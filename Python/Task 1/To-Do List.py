# To-Do List Program

todo_list = []

def show_todo_list():
    print("To-Do List:")
    for i, task in enumerate(todo_list, 1):
        print(f"{i}. {task}")

def add_task():
    task = input("Enter a task: ")
    todo_list.append(task)
    print(f"Task '{task}' added to the list.")

def delete_task():
    show_todo_list()
    task_number = int(input("Enter the task number to delete: ")) - 1
    if task_number < len(todo_list):
        del todo_list[task_number]
        print("Task deleted.")
    else:
        print("Invalid task number.")

while True:
    print("\n1. Show To-Do List")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Quit")
    choice = input("Choose an option: ")
    
    if choice == "1":
        show_todo_list()
    elif choice == "2":
        add_task()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please choose a valid option.")