try:
    data = open(
        "/home/odinproject/repos/Learning-Python-Projects/1. TODO list/tasks.txt", "r"
    ).readlines()
    task_list = [line.strip("\n") for line in data]
except FileNotFoundError:
    data = open(
        "/home/odinproject/repos/Learning-Python-Projects/1. TODO list/tasks.txt", "x"
    )
    task_list = []

exit = False


def view_tasks(task_list):
    for index, task in enumerate(task_list):
        print(f"{index}. {task}")


def save_task(task_list):
    with open(
        "/home/odinproject/repos/Learning-Python-Projects/1. TODO list/tasks.txt", "w"
    ) as f:
        for line in task_list:
            f.write(f"{line}\n")


def add_task(task_list):
    task_name = input("What's the task?:")
    task_list.append(task_name)


def remove_task(task_list):
    for index, task in enumerate(task_list):
        print(f"{index}. {task}")
    task_number = input(
        "Which task would you like to remove? (press enter to cancel)\n"
    )
    if task_number == "":
        pass
    else:
        task_list.remove(task_list[int(task_number)])


def display():
    global exit
    user_choice = input(
        """
    Type "view" to view your task list.
    Type "add" to add a new task
    Type "remove" to remove a task.
    Type "exit" to quit the program.
    """
    )
    if user_choice.lower() == "exit":
        exit = True
        save_task(task_list)
    elif user_choice.lower() == "save":
        save_task(task_list)
    elif user_choice == "view":
        view_tasks(task_list)
        input("Press enter to continue...")
    elif user_choice == "add":
        add_task(task_list)
        print("Task has been added!")
    elif user_choice == "remove":
        remove_task(task_list)


while exit == False:
    print("Welcome to your task list!")
    display()
