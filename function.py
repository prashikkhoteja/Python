def add_students():
    name = input("Name:")
    marks = int(input("Marks:"))
    students[name] = marks


students = {}
add_students()
print(students)
