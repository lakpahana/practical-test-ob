from django.contrib import admin

# Register your models here.

from .models import School, AssessmentAreas,CorrectAnswers, Awards, Class, Student, Subject, Answers, Summary

admin.site.register(School)
admin.site.register(AssessmentAreas)
admin.site.register(Awards)
admin.site.register(Class)
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Answers)
admin.site.register(Summary)
admin.site.register(CorrectAnswers)
