from Lab31 import Student
from Lab31 import get_LineAndObjects

lines = get_LineAndObjects.get_lines("students.txt")

students = get_LineAndObjects.get_objects(lines)

for student in sorted(students, key=lambda st: st.sred, reverse=True)[:3]:
    print(student)
