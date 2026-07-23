print("--------------------------")
print("Student Management System")
print("-------------------------")
students = {}
try:
    with open("Students.txt", "r") as file:
        for line in file:
            name, marks = line.strip().split(":")
            students[name] = int(marks)
except FileNotFoundError:
    print("\"File not found.\"")

if len(students) == 0:
    print("\nNo Students Found.")
    print("Add Students first.")
else:
    print("Student loaded successfully.")

while True:
    print("\nEnter 1 to Add more students:")
    print("Enter 2 to view the students:")
    print("Enter 3 to update the data of the existing student:")
    print("Enter 4 to search the data of the student:")
    print("Enter 5 to delete the data of the student:")
    print("Enter 6 to Exit:")
    print("\n")
    choice = int(input("Enter your choice: "))
    print("\n")
    if choice == 1:
        j = int(input("Enter the number of students: "))
        print("\n")
        for b in range(j):
            name = input(f"Enter the name of student number {b+1}: ").lower()
            students[name] = int(
                input(f"Enter the marks of the student {b+1}: "))
            print("\n")

    elif choice == 2:
        for name, marks in students.items():
            print(f"{name} : {marks}")

    elif choice == 3:
        name = input("Enter the name of the students: ").lower()
        if name in students.keys():
            updated_marks = int(input("Enter the Updated marks: "))
            students[name] = updated_marks
            print("Marks Updated")
        else:
            print("Student Not Found")
        print("\n")

    elif choice == 4:
        search = input("Enter the name you want to search:").lower()
        if search in students:
            print(
                f"The marks of the students named \"{search}\" is {students[search]}.")
        else:
            print("Student not found")
        print("\n")

    elif choice == 5:
        name = input("Enter the student name to delete:").lower()
        if name in students.keys():
            del students[name]
            print("Student data deleted.")
        else:
            print("Student Not Found")

    elif choice == 6:
        break


with open("Students.txt", "a") as file:

    for name, marks in students.items():
        file.write(f"{name}:{marks}\n")
