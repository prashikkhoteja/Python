print("-------------------------")
print("Student Management System")
print("-------------------------")
i = int(input("Enter the number of students: "))
print("\n")
print("Enter the details of the students")
student = []
for a in range(i):
    name = input(f"Enter the name of student {a+1}: ")
    age = int(input(f"Enter the age of student {a+1}: "))
    marks = int(input(f"Enter the marks of the student {a+1}: "))
    student.append([name, age, marks])
    print("\n")
for a in range(i):
    print(f"Details of student {a+1} :")
    print(f"Name : {student[a][0]}")
    print(f"Age : {student[a][1]}")
    print(f"Marks : {student[a][2]}")
    if student[a][2] >= 40:
        print("The student has passed the examination.")
    else:
        print("The student has failed the examination.")
    print("\n")
