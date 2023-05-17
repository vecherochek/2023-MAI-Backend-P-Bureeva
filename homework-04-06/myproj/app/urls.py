"""myproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.urls import path
from . import views

urlpatterns = [
    path('all_students/', views.all_students, name='all_students'),
    path('all_subjects/', views.all_subjects, name='all_subjects'),
    path('all_transcripts/', views.all_transcripts, name='all_transcripts'),
    path('student/<int:student_id>/', views.student, name='student'),
    path('subject/<int:subject_id>/', views.subject, name='subject'),
    path('transcript/<int:transcript_id>/', views.transcript, name='transcript'),
    path('search_students', views.search_students, name='search'),
    path('create_subject/', views.create_subject, name='create_subject'),

    path('subjects/', views.SubjectList.as_view(), name='subject-list'),
    path('subjects/<int:pk>/', views.SubjectDetail.as_view(), name='subject-detail'),
    path('students/', views.StudentList.as_view(), name='student-list'),
    path('students/<int:pk>/', views.StudentDetail.as_view(), name='student-detail'),
    path('transcripts/', views.TranscriptList.as_view(), name='transcript-list'),
    path('transcripts/<int:pk>/', views.TranscriptDetail.as_view(), name='transcript-detail'),

]

