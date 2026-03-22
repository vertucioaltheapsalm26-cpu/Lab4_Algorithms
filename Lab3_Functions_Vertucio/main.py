# main.py

import grades

# Student Identity Configuration
LAST_NAME = "Vertucio"
STUDENT_ID = "TUPM-24-4535"

# Logic for unique scores
SEED_DIGIT = int(STUDENT_ID[-1])
ID_SUM = sum(int(d) for d in STUDENT_ID if d.isdigit())
NAME_LENGTH = len(LAST_NAME)

# Generate student-unique scores
scores = [
    SEED_DIGIT * 10,
    ID_SUM % 100,
    NAME_LENGTH * 7
]

# FIX: Rename result variables to avoid overwriting the 'grades' module
avg_score = grades.compute_average(scores)
final_grade = grades.assign_grade(avg_score)
student_remark = grades.generate_remark(final_grade)

print("=" * 40)
print(f"Student: {LAST_NAME}")
print(f"Student ID: {STUDENT_ID}")
print(f"Generated Scores: {scores}")
print(f"Average: {round(avg_score, 2)}")
print(f"Grade: {final_grade}")
print(f"Remark: {student_remark}")
print("=" * 40)