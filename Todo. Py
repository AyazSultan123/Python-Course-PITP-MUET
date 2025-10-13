FILE_NAME = "tasks.txt"

# Add a new task
def add_task(task):
    with open(FILE_NAME, "a") as f:
        f.write(task + "\n")
    print(f"Task '{task}' added successfully!")

# View all tasks
def view_tasks():
    try:
        with open(FILE_NAME, "r") as f:
            tasks = f.readlines()

        if not tasks:
            print("No tasks found! Your to-do list is empty.")
        else:
            print("\nYour To-Do List:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task.strip()}")
    except FileNotFoundError:
        print("Task file not found. No tasks yet!")

# Update a task
def update_task(task_no, new_task):
    try:
        with open(FILE_NAME, "r") as f:
            tasks = f.readlines()

        if task_no <= 0 or task_no > len(tasks):
            print("Invalid task number!")
            return

        tasks[task_no - 1] = new_task + "\n"

        with open(FILE_NAME, "w") as f:
            f.writelines(tasks)

        print(f"Task {task_no} updated to '{new_task}'")
    except FileNotFoundError:
        print("No tasks to update! File not found.")

# Delete a task
def delete_task(task_no):
    try:
        with open(FILE_NAME, "r") as f:
            tasks = f.readlines()

        if task_no <= 0 or task_no > len(tasks):
            print("Invalid task number!")
            return

        removed = tasks.pop(task_no - 1)

        with open(FILE_NAME, "w") as f:
            f.writelines(tasks)

        print(f"Task '{removed.strip()}' deleted.")
    except FileNotFoundError:
        print("No tasks to delete! File not found.")

# Main menu
def main():
    while True:
        print("\n--- To-Do List Manager ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            view_tasks()

        elif choice == "2":
            task = input("Enter new task: ")
            add_task(task)

        elif choice == "3":
            view_tasks()
            try:
                task_no = int(input("Enter task number to update: "))
                new_task = input("Enter new task: ")
                update_task(task_no, new_task)
            except ValueError:
                print("Invalid input! Enter a number.")

        elif choice == "4":
            view_tasks()
            try:
                task_no = int(input("Enter task number to delete: "))
                delete_task(task_no)
            except ValueError:
                print("Invalid input! Enter a number.")

        elif choice == "5":
            print("Exiting To-Do List Manager. Goodbye!")
            break

        else:
            print("Invalid choice! Please enter 1-5.")

if __name__ == "__main__":
    main()
