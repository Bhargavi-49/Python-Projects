tasks = [ ]
while True:
    print("<---Task List--->")
    print("1.Add task")
    print("2.View tasks")
    print("3.Delete task")
    print("4.Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        task_name = input("Enter your task's name: ")
        tasks.append(task_name)
    elif choice == "2":
        for task in tasks:
            print(task)
    elif choice == "3":
        task_to_delete = input("Enter your task's name to delete: ")

        if task_to_delete  in tasks:
            tasks.remove(task_to_delete)
        else:
            print("Task not found")
    elif choice == "4":
        break
    else:
        print("Invalid choice")