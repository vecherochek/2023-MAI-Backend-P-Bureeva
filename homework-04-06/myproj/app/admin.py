from django.contrib import admin
from .models import Subject, Student, Transcript

admin.site.register(Subject)
admin.site.register(Student)
admin.site.register(Transcript)