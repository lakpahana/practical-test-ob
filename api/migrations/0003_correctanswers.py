# Generated by Django 5.0.3 on 2024-05-09 09:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rename_score_subject_subject_score'),
    ]

    operations = [
        migrations.CreateModel(
            name='CorrectAnswers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_number', models.IntegerField()),
                ('correct_answer', models.CharField(max_length=2)),
                ('assessment_area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='correct_answers', to='api.assessmentareas')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='correct_answers', to='api.subject')),
            ],
        ),
    ]
