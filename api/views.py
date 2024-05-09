from django.shortcuts import render
from django.core.paginator import Paginator
from .models import School, AssessmentAreas, Awards, Class, Student, Subject, Answers, Summary

# views.py
def index(request):
    # Get all objects
    schools = School.objects.all()
    assessment_areas = AssessmentAreas.objects.all()
    awards = Awards.objects.all()
    classes = Class.objects.all()
    students = Student.objects.all()
    subjects = Subject.objects.all()
    answers = Answers.objects.all()
    summaries = Summary.objects.all()

    # Create a Paginator object for each model
    schools_paginator = Paginator(schools, 10)  # Show 10 schools per page
    assessment_areas_paginator = Paginator(assessment_areas, 10)  # Show 10 assessment areas per page
    awards_paginator = Paginator(awards, 10)  # Show 10 awards per page
    classes_paginator = Paginator(classes, 10)  # Show 10 classes per page
    students_paginator = Paginator(students, 10)  # Show 10 students per page
    subjects_paginator = Paginator(subjects, 10)  # Show 10 subjects per page
    answers_paginator = Paginator(answers, 10)  # Show 10 answers per page
    summaries_paginator = Paginator(summaries, 10)  # Show 10 summaries per page

    # Get the page number from the query string for each paginator
    schools_page_number = request.GET.get('schools_page')
    assessment_areas_page_number = request.GET.get('assessment_areas_page')
    awards_page_number = request.GET.get('awards_page')
    classes_page_number = request.GET.get('classes_page')
    students_page_number = request.GET.get('students_page')
    subjects_page_number = request.GET.get('subjects_page')
    answers_page_number = request.GET.get('answers_page')
    summaries_page_number = request.GET.get('summaries_page')

    # Get the Page object for this page for each paginator
    schools_page = schools_paginator.get_page(schools_page_number)
    assessment_areas_page = assessment_areas_paginator.get_page(assessment_areas_page_number)
    awards_page = awards_paginator.get_page(awards_page_number)
    classes_page = classes_paginator.get_page(classes_page_number)
    students_page = students_paginator.get_page(students_page_number)
    subjects_page = subjects_paginator.get_page(subjects_page_number)
    answers_page = answers_paginator.get_page(answers_page_number)
    summaries_page = summaries_paginator.get_page(summaries_page_number)

    context = {
        'schools': schools_page,
        'assessment_areas': assessment_areas_page,
        'awards': awards_page,
        'classes': classes_page,
        'students': students_page,
        'subjects': subjects_page,
        'answers': answers_page,
        'summaries': summaries_page,
    }

    return render(request, 'index.html', context)