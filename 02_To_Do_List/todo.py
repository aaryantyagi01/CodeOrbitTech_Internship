# To-Do List CLI App
# CodeOrbit Tech Python Programming Internship

tasks = []


def add_task():
    task = input("Enter a task: ")

    if task.strip():
        tasks.append(task)
        print("Task added successfully!")
    else:
        print("Task cannot be empty.")


def view_tasks():
    if not tasks:
        print("No tasks available.")
        return

    print("\nYour Tasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")


def remove_task():
    if not tasks:
        print("No tasks available to remove.")
        return

    view_tasks()

    try:
        task_number = int(input("Enter task number to remove: "))

        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            print(f"Task removed: {removed_task}")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


def main():
    while True:
        print("\n===== TO-DO LIST =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task()

        elif choice == "2":
            view_tasks()

        elif choice == "3":
            remove_task()

        elif choice == "4":
            print("Thank you for using To-Do List!")
            break

        else:
            print("Invalid choice. Please try again.")


main()