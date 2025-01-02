def read_tasks(file_path):
    try:
        with open(file_path, 'r') as file:
            tasks = [line.strip() for line in file.readlines()]
        return tasks
    except FileNotFoundError:
        print("File not found. Starting with an empty task list.")
        return []
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return []

def write_tasks(file_path, tasks):
    try:
        with open(file_path, 'w') as file:
            for task in tasks:
                file.write(f"{task}\n")
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")

def add_task(tasks):
    task = input("Enter a new task: ")
    tasks.append(task)
    print(f"Task '{task}' added.")

def remove_task(tasks):
    task = input("Enter the task to remove: ")
    if task in tasks:
        tasks.remove(task)
        print(f"Task '{task}' removed.")
    else:
        print(f"Task '{task}' not found.")

def view_tasks(tasks):
    if tasks:
        print("Your tasks:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")
    else:
        print("No tasks found.")

def main():
    file_path = 'tasks.txt'
    tasks = read_tasks(file_path)

    while True:
        print("\nTask List Manager")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            remove_task(tasks)
        elif choice == '3':
            view_tasks(tasks)
        elif choice == '4':
            write_tasks(file_path, tasks)
            print("Tasks saved. Exiting.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()