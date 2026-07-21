students = {}

while True:
    print("1.Add new students:")
    print("2.View  students")
    print("3.exit")

    choice = int(input("Enter the number of your choice i.e 1, 2 or 3: "))
    if choice == 1:
        name = input("Name:")
        students[name] = int(input("Marks:"))

    elif choice == 2:
        print(students)
        print("\n")
    elif choice == 3:
        break
