students = {}

for a in range(2):
    name = input("Name: ")
    marks = int(input("Marks: "))
    students[name] = marks

with open("Studentssss.txt", "w") as file:

    for name, marks in students.items():
        file.write(f"{name}:{marks} \n")
