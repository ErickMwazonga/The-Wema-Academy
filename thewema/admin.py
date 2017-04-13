from django.contrib import admin
from .models import Student, StudentClass, Subject, Exam, Score, Feedback
# Register your models here.

admin.site.register(Student)
admin.site.register(StudentClass)
admin.site.register(Subject)
admin.site.register(Exam)
admin.site.register(Score)
admin.site.register(Feedback)
