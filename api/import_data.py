import pandas as pd
import os
import glob
from api.models import School, Student, Subject, AssessmentAreas, Awards, Class, Answers, Summary,CorrectAnswers

def import_data():
    csv_directory = "api/dataset/"
    csv_files = glob.glob(os.path.join(csv_directory, "*.csv"))
    batch_size = 10000
    row_num= "";
    for csv_file in csv_files:
        print(f"Processing data from {csv_file}")
        try:
            for chunk in pd.read_csv(csv_file, chunksize=batch_size):
                # print(f"Processing {batch_size}  rows")
                # remaining_rows = len(chunk)
                print(f"Processing {len(chunk)} rows")
                chunk_size = len(chunk)

                for index, row in chunk.iterrows():
                    row_num = row
                    print(f"Processing row {index + 1} of {chunk_size}")

                    school, _ = School.objects.get_or_create(
                            name=row["school_name"]
                    )

                    # Create or retrieve a Class object based on the class name
                    class_name = row["Class"]
                    class_instance, _ = Class.objects.get_or_create(
                        class_name=class_name
                    )

                    # Create or retrieve an AssessmentArea object based on the Assessment Area name
                    assessment_area_name = row["Assessment Areas"]
                    assessment_area, _ = AssessmentAreas.objects.get_or_create(
                        name=assessment_area_name
                    )

                    # Create a unique student identifier based on StudentID
                    student_identifier = row["StudentID"]
                    # Create or retrieve a Student object based on the unique identifier
                    student, _ = Student.objects.get_or_create(
                        id=student_identifier,
                        defaults={
                            "fullname": f"{row['First Name']} {row['Last Name']}",
                        },
                    )

                    answer_value = row["Answers"]
                    answers_instances = Answers.objects.filter(answers=answer_value)

                    if answers_instances.exists():
                        answers_instance = answers_instances.first()
                    else:
                        # If it doesn't exist, create a new Answers object
                        answers_instance = Answers.objects.create(
                            answers=answer_value
                        )

               
                    awards_name = row.get("award") or row.get("awarDistinction")
                    awards_instance, _ = Awards.objects.get_or_create(
                        name=awards_name
                    )

                    # Create or retrieve a Subject object based on the subject name
                    subject_name = row["Subject"]
                    subject_instance, _ = Subject.objects.get_or_create(
                        subject=subject_name,
                        defaults={"subject_score": row["student_score"]},
                    )



                    # Create or retrieve a CorrectAnswers object based on the assessment area, subject, and question number
                    correct_answer_instances = CorrectAnswers.objects.filter(
                        assessment_area=assessment_area,
                        subject=subject_instance,
                        question_number=row["Question Number"],
                    )

                    if correct_answer_instances.exists():
                        correct_answer_instance = correct_answer_instances.first()
                    else:
                        # If it doesn't exist, create a new CorrectAnswers object
                        correct_answer_instance = CorrectAnswers.objects.create(
                            assessment_area=assessment_area,
                            subject=subject_instance,
                            question_number=row["Question Number"],
                            correct_answer=row["Correct Answers"],
                        )




                    Summary.objects.create(
                        school=school,
                        sydney_participant=row["sydney_participants"],
                        sydney_percentile=row["sydney_percentile"],
                        assessment_area=assessment_area,
                        award=awards_instance,
                        class_id=class_instance,
                        correct_answer_percentage_per_class=row["correct_answer_percentage_per_class"],
                        answer=answers_instance,
                        correct_answer=correct_answer_instance,
                        student=student,
                        student_score=row["student_score"],
                        subject=subject_instance,
                        category_id=row["Question Number"],
                        year_level_name=row["Year Level"],
                        participant=row["participant"],
                        correct_answer_id=correct_answer_instance.id,
                    )

        except Exception as e:  # Use except instead of catch
            # Print the error message which row 
            print(f"Error processing data from {csv_file} in row {row_num}: {str(e)}")

            # print(f"Error processing data from {csv_file}: {str(e)}")
            continue
        print(f"Successfully processed data from {csv_file}")
