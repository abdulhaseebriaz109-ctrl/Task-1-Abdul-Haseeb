# Simple To-Do List Program

tasks = []

while True:
    print("\n------ TO-DO LIST ------")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter your task: ")
        tasks.append(task)
        print("Task Added Successfully!")

    elif choice == "2":
        if tasks == []:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            count = 1
            for task in tasks:
                print(count, "-", task)
                count = count + 1

    elif choice == "3":
        print("Program Closed.")
        break

    else:
        print("Invalid Choice! Please try again.")