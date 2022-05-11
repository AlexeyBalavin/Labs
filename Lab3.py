from Lab31 import Student
from Lab31 import get_LineAndObjects

lines = get_lines("students.txt")

students = get_objects(lines)

for student in sorted(students, key=lambda st: st.sred, reverse=True)[:3]:
    print(student)
