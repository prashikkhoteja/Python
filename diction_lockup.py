# Dictionary look up / Search Student
student = {}
for i in range(2):
    name = input("Name: ")
    marks = int(input("Marks: "))
    student[name] = marks
print(student)
search = input("Search student: ")
if search in student:
    print(student[search])
else:
    print("Student not found")
