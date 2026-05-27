students = [
    {"name": "Mishti", "score": 92},
    {"name": "Aman", "score": 81},
    {"name": "Riya", "score": 74},
    {"name": "Rahul", "score": 65},
    {"name": "Karan", "score": 45}
]


def classify(score):

    if score >= 90:
        return "A"

    elif score >= 80:
        return "B"

    elif score >= 70:
        return "C"

    elif score >= 60:
        return "D"

    else:
        return "F"


# Sorting students from highest to lowest score
sorted_students = sorted(
    students,
    key=lambda student: student["score"],
    reverse=True
)

# Printing name and grade
for student in sorted_students:

    grade = classify(student["score"])

    print(f"{student['name']} : {grade}")