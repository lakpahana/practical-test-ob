from django.db import models

class School(models.Model):
    name = models.CharField(max_length=200)

class AssessmentAreas(models.Model):
    name = models.CharField(max_length=200)

class Awards(models.Model):
    name = models.CharField(max_length=200)

class Class(models.Model):
    class_name = models.CharField(max_length=200)

class Student(models.Model):
    fullname = models.CharField(max_length=200)

class Subject(models.Model):
    subject = models.CharField(max_length=200)
    subject_score = models.IntegerField()

class Answers(models.Model):
    answers = models.CharField(max_length=200)
# school_name,year,StudentID,First Name,Last Name,Year Level,Class,Subject,Answers,Correct Answers,Question Number,Subject Contents,Assessment Areas,sydney_correct_count_percentage,sydney_average_score,sydney_participants,student_score,student_total_assessed,student_area_assessed_score,total_area_assessed_score,participant,correct_answer_percentage_per_class,average_score,school_percentile,sydney_percentile,strength_status,high_distinct_count,distinct_count,credit_count,participant_count,award
# "Christ King Catholic School, Bass Hill",2022,1,First Name 1,Last Name 1,2,Class 2,Science,D,?,48,Subject Content 1 for Science,Assessment Area 1 for Science,93.56,78.75,49,26.73,87,3.2,28.42,86,72.28,16.06,28,47,-,24,36,8,25,High Distinction
class CorrectAnswers(models.Model):
    assessment_area = models.ForeignKey(AssessmentAreas, on_delete=models.CASCADE, related_name='correct_answers')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='correct_answers')
    question_number = models.IntegerField()
    # Correct answers can uniquely identify using above fields
    
    correct_answer = models.CharField(max_length=2)



class Summary(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='summaries')
    sydney_participant = models.IntegerField()
    sydney_percentile = models.FloatField()
    assessment_area = models.ForeignKey(AssessmentAreas, on_delete=models.CASCADE, related_name='summaries')
    award = models.ForeignKey(Awards, on_delete=models.CASCADE, related_name='summaries')
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='summaries')
    correct_answer_percentage_per_class = models.FloatField()
    answer = models.ForeignKey(Answers, on_delete=models.CASCADE, related_name='summaries')
    correct_answer = models.CharField(max_length=2)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='summaries')
    student_score = models.IntegerField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='summaries')
    category_id = models.IntegerField()
    year_level_name = models.CharField(max_length=200)
    participant = models.IntegerField()
    correct_answer_id = models.IntegerField()