from .models import Student, StudentClass, Exam, Score, Subject, Feedback
from django import forms
from django.contrib.auth.models import User
# from django.core.validators import ValidationError

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, MultiWidgetField, Submit


class StudentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))

        self.helper.layout = Layout(
            'admin_no',
            'first_name',
            'middle_name',
            'surname',
            'gender',
            MultiWidgetField(
                'dob',
                attrs=(
                    {'style': 'width: 30%; display: inline-block;'}
                )
            ),
            'sclass',
            'image'

        )

    class Meta:
        model = Student
        fields = ['admin_no', 'first_name', 'middle_name', 'surname',
                  'gender', 'dob', 'sclass', 'image']

        widgets = {
            'dob': forms.SelectDateWidget(years=[str(val) for val in range(1998, 2005)]),
            }

        help_texts = {
            'dob': 'Enter the day you saw the world'
        }

        labels = {
            'dob': 'Date of Birth',
            'sclass': 'Class',
            'admin_no': 'Admission Number'
        }


class StudentClassForm(forms.ModelForm):
    class Meta:
        model = StudentClass
        fields = ['standard', 'year', 'teacher']


class ExamForm(forms.ModelForm):
    class Meta:
        model = Exam
        fields = ['term', 'etype']

        labels = {
            'etype': 'Type'
        }


class ScoreForm(forms.ModelForm):
    class Meta:
        model = Score
        fields = ['student', 'subject', 'exam', 'marks']

        # labels = {
        #     'sclass': 'Class'
        # }


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

        help_texts = {
            'username': ' '
        }


class StudentSearchForm(forms.Form):

    form = forms.ModelChoiceField(
        queryset=StudentClass.objects.all(),
        required=False,
        empty_label='Select Class',
    )
    name = forms.CharField(
        max_length=100,
        required=False,
        help_text='Search by first name, second name or last name'
    )

    def __init__(self, *args, **kwargs):
        super(StudentSearchForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-inline'
        self.helper.field_template = 'bootstrap3/layout/inline_field.html'
        self.helper.layout = Layout(
            'name',
            'form',
            Submit('Search', 'search', css_class='btn-default'),
        )
        self.helper.form_method = 'get'

    def get_queryset_filters(self):
        filters = {}
        if self.is_valid():
            name = self.cleaned_data.get('name')
            filters['name'] = name


class ScoreSearchForm(forms.Form):

    name = forms.CharField(
        max_length=100,
        required=False,
        help_text='Search by first name, middle_name or last name'
    )
    form = forms.ModelChoiceField(
        queryset=StudentClass.objects.all(),
        required=False,
        empty_label='Select Class',
    )
    subject = forms.ModelChoiceField(
        queryset=Subject.objects.all(),
        required=False,
        empty_label='Select Subject',
    )

    def __init__(self, *args, **kwargs):
        super(ScoreSearchForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-inline'
        self.helper.field_template = 'bootstrap3/layout/inline_field.html'
        self.helper.layout = Layout(
            'name',
            'form',
            'subject',
            Submit('Search', 'search', css_class='btn-default'),
        )
        self.helper.form_method = 'get'

    def get_queryset_filters(self):
        filters = {}
        if self.is_valid():
            name = self.cleaned_data.get('name')
            filters['name'] = name


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'subject', 'message']
