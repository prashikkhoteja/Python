students = {}

with open("Students.txt", "r") as file:
    for line in file:
        name, marks = line.strip().split(",")
        students[name] = int(marks)

print(students)
