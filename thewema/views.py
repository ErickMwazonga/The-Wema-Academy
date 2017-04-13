from django.shortcuts import redirect
from django.http import HttpResponse
# from django.conf import settings
from .models import Student, StudentClass, Exam, Score, Feedback
from .forms import StudentForm, StudentClassForm, ExamForm, ScoreForm, FeedbackForm, StudentSearchForm, ScoreSearchForm
from django.views.generic import ListView, CreateView, DetailView, TemplateView
from django.core.urlresolvers import reverse
from django.db.models import Sum, Q

from django.views import View
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
# from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.core.mail import send_mail, BadHeaderError


# Student Views

class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'thewema/index.html'


class StudentListView(LoginRequiredMixin,  ListView):
    context_object_name = 'student_list'
    model = Student
    template_name = 'thewema/student_list.html'
    paginate_by = 8

    # def get_queryset(self):
    #     return Student.objects.all()

    def get_queryset(self):
        queryset = super(StudentListView, self).get_queryset().order_by('-first_name')

        by_name = self.request.GET.get('name')
        by_form = self.request.GET.get('form')

        if by_form and by_name:
            return queryset.filter(
                Q(first_name__contains=by_name) | Q(surname__contains=by_name) | Q(middle_name__contains=by_name),
                sclass__id=by_form
            )
        if by_name:
            return queryset.filter(
                Q(first_name__contains=by_name) | Q(surname__contains=by_name) | Q(middle_name=by_name)
            )
        if by_form:
            return queryset.filter(
                sclass__id=by_form
            )
        return queryset
    def get_context_data(self, **kwargs):
        cxt = super(StudentListView, self).get_context_data(**kwargs)
        cxt['search_form'] = StudentSearchForm()
        return cxt


class StudentCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Student
    template_name = 'thewema/student_form.html'
    form_class = StudentForm
    success_message = "Student Added successfully"

    def get_success_url(self):
        return reverse('thewema:students')


class StudentDetailView(LoginRequiredMixin, DetailView):
    model = Student
    template_name = 'thewema/student_detail.html'

    def get_success_url(self):
        return reverse('thewema: students')


class StudentClassCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = StudentClass
    form_class = StudentClassForm
    template_name = 'thewema/studentclass_form.html'
    success_message = "Class Created successfully"

    def get_success_url(self):
        return reverse('thewema:classes')


class StudentClassListView(LoginRequiredMixin, ListView):
    context_object_name = 'studentclass_list'
    model = StudentClass
    template_name = 'studentclass_list.html'

    def get_queryset(self):
        return StudentClass.objects.all()


class ExamCreateView(LoginRequiredMixin, CreateView):
    model = Exam
    template_name = 'thewema/exam_form.html'
    form_class = ExamForm

    def get_success_url(self):
        return reverse('thewema:index')


class ScoreCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Score
    template_name = 'thewema/score_form.html'
    form_class = ScoreForm
    success_message = "Score Entered Successfully"

    def get_success_url(self):
        return reverse('thewema:scores')


class ScoreListView(LoginRequiredMixin, ListView):
    model = Score
    template_name = 'thewema/score_list.html'
    context_object_name = 'score_list'
    paginate_by = 8

    def get_queryset(self):
        queryset = super(ScoreListView, self).get_queryset().order_by('-marks')

        by_name = self.request.GET.get('name')
        by_form = self.request.GET.get('form')
        by_subject = self.request.GET.get('subject')

        if by_form and by_name and by_subject:
            return queryset.filter(
                Q(student__first_name__contains=by_name) | Q(student__surname__contains=by_name) | Q(student__middle_name__contains=by_name),
                sclass__id=by_form,
                subject__id=by_subject
            )
        if by_name:
            return queryset.filter(
                Q(student__first_name__contains=by_name) | Q(student__surname__contains=by_name) | Q(student__middle_name=by_name)
            )
        if by_form:
            return queryset.filter(
                student__sclass__id=by_form
            )
        if by_subject:
            return queryset.filter(
                subject__id=by_subject
            )
        return queryset

    def get_context_data(self, **kwargs):
        cxt = super(ScoreListView, self).get_context_data(**kwargs)
        cxt['search_form'] = ScoreSearchForm()
        return cxt


class ScoreDetailView(LoginRequiredMixin, ListView):
    template_name = 'thewema/score_details.html'
    context_object_name = 'student_scores_list'

    def get_queryset(self):
        qs = Score.objects.filter(
            student__id=self.kwargs['pk'],
            exam=Exam.objects.last()
            )
        return qs

    def get_context_data(self, **kwargs):
        ctx = super(ScoreDetailView, self).get_context_data(**kwargs)
        total = Score.objects.filter(
            student__id=self.kwargs['pk'],
            exam=Exam.objects.last()
            ).aggregate(total=Sum('marks'))
        ctx['total'] = total
        return ctx


def logout_view(request):
    logout(request)
    return redirect('thewema:index')


class LoginView(View):
    template_name = 'thewema/login.html'
    authentication_form = AuthenticationForm

    def get(self, request):
        return login(
            request,
        )


class FeedbackCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Feedback
    form_class = FeedbackForm
    template_name = "thewema/feedback_form.html"
    success_message = "Thank you for your Feedback"

    def get_success_url(self):
        return reverse("thewema:index")

    def send_email(self):
        name = self.request.POST.get('name')
        subject = self.request.POST.get('subject')
        message = self.request.POST.get('message')
        from_email = self.request.POST.get('email')

        if subject and message and from_email:
            try:
                send_mail(subject, message, from_email, ['erickmwazonga@gmail.com'], fail_silently=False,)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return reverse("thewema:index")
        else:
            # In reality we'd use a form class
            # to get proper validation errors.
            return HttpResponse('Make sure all fields are entered and valid.')

    def form_valid(self, form):
        self.send_email()
        return super(FeedbackCreateView, self).form_valid(form)


# @login_required(login_url="thewema:login")
# def index_view(request):
#     return render(
#         request,
#         'thewema/index.html',
#         {
#             'school_name': settings.SCHOOL_NAME,
#             'school_motto': settings.SCHOOL_MOTTO
#         }
#     )


# class UserFormView(View):
#     form_class = UserForm
#
#     template_name = 'thewema/registration_form.html'
#
#     # display a blank form
#     def get(self, request):
#         form = self.form_class(None)
#         return render(request, self.template_name, {'form': form})
#
#     # process form data
#     def post(self, request):
#         form = self.form_class(request.POST)
#
#         if form.is_valid():
#
#             user = form.save(commit=False)
#
#             # cleaned (normalized) data
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user.set_password(password)
#             user.save()
#
#             # returns User objects if credentials are correct
#             user = authenticate(username=username, password=password)
#
#             if user is not None:
#
#                 if user.is_active:
#                     login(request, user)
#                     return redirect('thewema:index')
#
#         return render(request, self.template_name, {'form': form})
