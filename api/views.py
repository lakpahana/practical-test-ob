from django.shortcuts import render
from django.core.paginator import Paginator
from .models import School, AssessmentAreas, Awards, Class, Student, Subject, Answers, Summary, CorrectAnswers

def paginate_query(request, query_set, count, page_query_param):
    paginator = Paginator(query_set, count)  
    page_number = request.GET.get(page_query_param)  
    return paginator.get_page(page_number)  

def index(request):    
    model_page_dict = {
        'schools': (School.objects.all(), 'schools_page', 10),
        'assessment_areas': (AssessmentAreas.objects.all(), 'assessment_areas_page', 10),
        'awards': (Awards.objects.all(), 'awards_page', 10),
        'classes': (Class.objects.all(), 'classes_page', 10),
        'students': (Student.objects.all(), 'students_page', 10),
        'subjects': (Subject.objects.all(), 'subjects_page', 10),
        'answers': (Answers.objects.all(), 'answers_page', 10),
        'summaries': (Summary.objects.all(), 'summaries_page', 10),
        'correct_answers': (CorrectAnswers.objects.all(), 'correct_answers_page', 10)
    }

    context = {}
    for key, value in model_page_dict.items():
        context[key] = paginate_query(request, value[0], value[2], value[1])  

    return render(request, 'index.html', context)
