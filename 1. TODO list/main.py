task_list = []
exit = False

def view_tasks(task_list):
    for index, task in enumerate(task_list):
        print(f"{index}. {task}")

def add_task(task_list):
    task_name = input("What's the task?:")
    task_list.append(task_name)

def remove_task(task_list):
    for index, task in enumerate(task_list):
        print(f"{index}. {task}")
    task_number = input("Which task would you like to remove? (press enter to cancel)")
    if task_number == "":
        pass
    else:
        task_list.remove(task_list[int(task_number)])
    
while exit == False:
    print("Hi! Welcome to your todo list. What would you like to do?")
    user_choice = input('''
    Press "1" to view your task list.
    Press "2" to add a new task
    Press "3" to remove a task.
    Type "exit" to quit the program.
    ''')
    if user_choice.lower() == "exit":
        exit = True 
    elif user_choice == "1":
        view_tasks(task_list)
        input("Press any key to continue...")
    elif user_choice == "2":
        add_task(task_list)
        pass
    elif user_choice == "3":
        remove_task(task_list)










