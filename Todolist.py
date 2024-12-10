todo_list = []
def add_task():
    task = input("Enter the task: ")
    todo_list.append(task)

def view_task():
    for task in todo_list:
        print(f"- {task}")

def remove_task():
    remove_task = input("Enter the task: ")
    for task in todo_list:
        if task == remove_task:
            todo_list.remove(task)

while True:
    action = input("Enetr your choice : add,view,remove,quit : ").lower()
    if action == 'add':
        add_task()
    elif action == 'view':
        view_task()
    elif action == 'remove':
        remove_task()
    elif action == 'quit':
        break
    else:
        print("Invalid Choice")
