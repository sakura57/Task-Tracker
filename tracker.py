import re
import json
import datetime

file_path = "tasks.json"
running = True
tasks = {}

# The following functions respond to each command.

def addTask(task_name):
    global tasks
    if tasks:
        id = max([int(key) for key in tasks.keys()]) + 1
        print("ID updated.")
    else:
        id = 1
        print("ID set to 1.")
    
    task = {
        "id": id,
        "description": task_name,
        "status": "todo",
        "createdAt": datetime.datetime.now().strftime("%A, %Y-%m-%d %H:%M:%S"),
        "updatedAt": datetime.datetime.now().strftime("%A, %Y-%m-%d %H:%M:%S")
    }

    tasks[str(id)] = task

    with open(file_path, "w") as json_file:
        json.dump(tasks, json_file, indent=4)

    print(f"Task added: {task_name}, ID:{id}")
    return id

def updateTask(id, task_name):
    global tasks
    for task_id in tasks:
        if task_id == id:
            tasks[id].update({"description": task_name})
            tasks[id].update({"updatedAt": datetime.datetime.now().strftime("%A, %Y-%m-%d %H:%M:%S")})
            print(f"Task {id} updated")
            break
    else:
        print("ID number not found.")

    with open(file_path, "w") as json_file:
        json.dump(tasks, json_file, indent=4)

def deleteTask(id):
    global tasks
    if id in tasks:
        del tasks[id]
        print(f"Task with ID {id} deleted.")

        new_tasks = {}
        for new_id, old_id in enumerate(sorted(tasks.keys(), key=int), start=1):
            task = tasks[old_id]
            task['id'] = new_id
            new_tasks[str(new_id)] = task

        tasks.clear()
        tasks.update(new_tasks)

        with open(file_path, "w") as json_file:
            json.dump(tasks, json_file, indent=4)

        print("Task IDs rearranged.")

    else:
        print(f"ID number {id} not found.")

def markInProgress(id):
    global tasks
    if id in tasks:
        tasks[id].update({"status": "in-progress"})
        tasks[id].update({"updatedAt": datetime.datetime.now().strftime("%A, %Y-%m-%d %H:%M:%S")})
        print(f"Task {id} is now in-progress.")
    else:
        print("ID number not found.")

    with open(file_path, "w") as json_file:
        json.dump(tasks, json_file, indent=4)

def markDone(id):
    global tasks
    if id in tasks:
        tasks[id].update({"status": "done"})
        tasks[id].update({"updatedAt": datetime.datetime.now().strftime("%A, %Y-%m-%d %H:%M:%S")})
        print(f"Task {id} is done.")
    else:
        print("ID number not found.")

    with open(file_path, "w") as json_file:
        json.dump(tasks, json_file, indent=4)

def list(status=None):
    found = False

    for outer_key, value in tasks.items():
        if status is None or status == value["status"]:
            found = True
            print()
            print(f"Task #{outer_key}")
            for key, value in value.items():
                print(f"{key}: {value}")
            print()
        else:
            continue
    if not found:
        err_text = "No tasks found." if status is None else f"No tasks found marked as {status}."
        print(err_text)

def process_input(user_input):#main function that identifies commands, and executes respective functions
    match_add = re.match(r'^add\s+"(.+)"$', user_input)
    match_update = re.match(r'^update\s+(\d+)\s+"(.+)"$', user_input)
    match_list = re.match(r'^list$', user_input)
    match_delete = re.match(r"^delete\s+(\d+)$", user_input)
    match_mkinpg = re.match(r'^mark-in-progress\s+(\d+)$', user_input)
    match_mkdone = re.match(r'^mark-done\s+(\d+)$', user_input)
    match_listdone = re.match(r'^list\s+(done)$', user_input)
    match_listtodo = re.match(r'^list\s+(todo)$', user_input)
    match_listinpgr = re.match(r'^list\s+(in-progress)$', user_input)
    if match_add:
        task_name = match_add.group(1)
        addTask(task_name)
    elif match_update:
        id = match_update.group(1)
        task_name = match_update.group(2)
        updateTask(id, task_name)
    elif match_delete:
        id = match_delete.group(1)
        deleteTask(id)
    elif match_mkinpg:
        id = match_mkinpg.group(1)
        markInProgress(id)
    elif match_mkdone:
        id = match_mkdone.group(1)
        markDone(id)
    elif match_list:
        list()
    elif match_listdone:
        status = match_listdone.group(1)
        list(status)
    elif match_listtodo:
        status = match_listtodo.group(1)
        list(status)
    elif match_listinpgr:
        status = match_listinpgr.group(1)
        list(status)
    else:
        print("Invalid command.")

with open(file_path, "r") as json_file: #loads data from JSON file
    try:
        tasks = json.load(json_file)
        print("Data successfully loaded.")
    except json.JSONDecodeError:
        tasks = {}
        print("The JSON file is empty or not properly formatted.")

while running: #CLI
    user_input = input("task-cli ")
    process_input(user_input)