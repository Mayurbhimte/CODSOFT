# Task 1 - To-Do List in Python

todo_list = []

def show_menu():
    print("\nTo-Do List Menu")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

def add_task():
    task = input("Enter the task: ")
    todo_list.append({'task': task, 'completed': False})
    print("Task added.")

def view_tasks():
    if not todo_list:
        print("No tasks yet.")
    else:
        print("\nYour Tasks:")
        for i, item in enumerate(todo_list, 1):
            status = "Completed" if item['completed'] else "Pending"
            print(f"{i}. {item['task']} [{status}]")

def mark_completed():
    view_tasks()
    try:
        task_num = int(input("Enter task number to mark complete: "))
        if 1 <= task_num <= len(todo_list):
            todo_list[task_num - 1]['completed'] = True
            print("Task marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task():
    view_tasks()
    try:
        task_num = int(input("Enter task number to delete: "))
        if 1 <= task_num <= len(todo_list):
            deleted = todo_list.pop(task_num - 1)
            print(f"Deleted task: {deleted['task']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

while True:
    show_menu()
    choice = input("Choose an option (1-5): ")

    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        mark_completed()
    elif choice == '4':
        delete_task()
    elif choice == '5':
        print("Exiting To-Do List. Goodbye.")
        break
    else:
        print("Invalid choice. Please choose again.")