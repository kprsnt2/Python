# Todo list application
tasks = []

def add_task(task):
    tasks.append(task)
    print("Task added:", task)

def edit_task(index, new_task):
    tasks[index] = new_task
    print("Task edited:", new_task)

def delete_task(index):
    task = tasks.pop(index)
    print("Task deleted:", task)

def view_all_tasks():
    for i, task in enumerate(tasks):
        print(i, task)

def save_tasks():
    with open("tasks.txt", "w") as f:
        for task in tasks:
            f.write(task + "\n")
    print("Tasks saved to tasks.txt")

def read_tasks():
    with open("tasks.txt", "r") as f:
        for line in f:
            tasks.append(line.strip())
    print("Tasks loaded from tasks.txt")
