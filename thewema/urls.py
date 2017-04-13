"""wema URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import AuthenticationForm

app_name = 'thewema'

urlpatterns = [
    # url(r'^$', views.index_view, name='index'),
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^students$', views.StudentListView.as_view(), name='students'),
    url(r'^student$', views.StudentCreateView.as_view(), name='student'),
    url(r'^student/(?P<pk>[0-9]+)/$', views.StudentDetailView.as_view(), name='student_detail'),
    url(r'^class$', views.StudentClassCreateView.as_view(), name='sclass'),
    url(r'^classes$', views.StudentClassListView.as_view(), name='classes'),
    url(r'^exam$', views.ExamCreateView.as_view(), name='exam'),
    url(r'^score$', views.ScoreCreateView.as_view(), name='score'),
    url(r'^scores$', views.ScoreListView.as_view(), name='scores'),
    url(r'^scores/(?P<pk>[0-9]+)/$', views.ScoreDetailView.as_view(), name='score_detail'),
    url(r'^feedback$', views.FeedbackCreateView.as_view(), name='feedback'),
    url(r'^login$', auth_views.login, {
            'template_name': 'thewema/login.html',
            'authentication_form': AuthenticationForm
        },
        name='login'
        ),
    url(r'^logout/$', auth_views.logout_then_login, {'login_url': 'thewema:login'}, name='logout'),
]
