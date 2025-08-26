import os
FILENAME = "tasks.txt"
tasks = []
def load_tasks():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as f:
            for line in f:
                task, status = line.strip().split("|")
                tasks.append({"task": task, "done": status == "True"})
def save_tasks():
    with open(FILENAME, "w") as f:
        for t in tasks:
            f.write(f"{t['task']}|{t['done']}\n")
def show_menu():
    print("\n=== To-Do List ===")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Task Completed")
    print("6. Exit")
def view_tasks():
    if not tasks:
        print("No tasks yet!")
    else:
        print("\nYour Tasks:")
        for i, t in enumerate(tasks, 1):
            status = " Done" if t["done"] else " Pending"
            print(f"{i}. {t['task']} [{status}]")
def add_task():
    task = input("Enter new task: ").strip()
    if task:
        tasks.append({"task": task, "done": False})
        print(" Task added!")
    else:
        print(" Empty task not allowed!")
def update_task():
    view_tasks()
    if tasks:
        try:
            num = int(input("Enter task number to update: "))
            new_task = input("Enter updated task: ").strip()
            tasks[num-1]["task"] = new_task
            print(" Task updated!")
        except (ValueError, IndexError):
            print(" Invalid task number!")
def delete_task():
    view_tasks()
    if tasks:
        try:
            num = int(input("Enter task number to delete: "))
            removed = tasks.pop(num-1)
            print(f" Task '{removed['task']}' deleted!")
        except (ValueError, IndexError):
            print(" Invalid task number!")
def complete_task():
    view_tasks()
    if tasks:
        try:
            num = int(input("Enter task number to mark completed: "))
            tasks[num-1]["done"] = True
            print(" Task marked as completed!")
        except (ValueError, IndexError):
            print(" Invalid task number!")
def main():
    load_tasks()
    while True:
        show_menu()
        choice = input("Enter choice (1-6): ").strip()
        
        if choice == "1":
            view_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            update_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            complete_task()
        elif choice == "6":
            save_tasks()
            print(" Exiting ")
            break
        else:
            print(" Invalid choice! Enter 1-6.")

if __name__ == "__main__":
    main()
