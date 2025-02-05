def sort_students_by_grade(students):
    sorted_students = sorted(students, key=lambda student: student[2])
    return sorted_students

students = (
    ("Ali", 20, 88),
    ("Babul", 22, 75),
    ("Carina", 19, 95),
    ("Daud", 21, 85)
)

sorted_students = sort_students_by_grade(students)
print(sorted_students)