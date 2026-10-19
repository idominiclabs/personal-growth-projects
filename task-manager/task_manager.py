#task manager
import json
import time

try:
    with open("task_database.json","r") as r_file:
        all_tasks = json.load(r_file)
except FileNotFoundError:
    with open("task_database.json","w") as w_file:
        json.dump([], w_file)
        
    with open("task_database.json","r") as r_file:
        all_tasks = json.load(r_file)
        
def save_file():
    with open("task_database.json", "w") as w_file:
        json.dump(all_tasks, w_file)
        
        
def add_task():
    title = input("Title: ").lower().strip()
    description = input("Description: ").lower().strip()
    priority = input("Priority (high/medium/low): ").lower().strip()
    due_date = input("Due date (format = yyyy/mm/dd): ").strip()
    
    if title and description and priority and due_date:
        priority_list = ["high","medium","low"]
        if priority in priority_list:
            task = {
                "title": title,
                "description": description,
                "priority": priority,
                "due_date": due_date,
                "status": "pending"
            }
            all_tasks.append(task)
            save_file()
            print("Task has been added successfully!")
         
        else:
            print("Invalid priority!")
        
    else:
        print("Incomplete fields, Enter valid characters only!")
        
        
def view_tasks(task_list):
    temp_base = []
    if task_list:
        for each_task in task_list:
            task_str = f"Title: {each_task.get("title").capitalize()}\nDescription: {each_task.get("description").capitalize()}\nPriority: {each_task.get("priority").title()}\nStatus: {each_task.get("status").capitalize()}\nDue date: {each_task.get("due_date")}\n"
            temp_base.append(task_str)
            
        print("All tasks")
        for number,task in enumerate(temp_base, start=1):
            print(f"{number}. {task}")
            
    else:
        print("Can't view, add task to view!")
            
            
def search_task():
    search_input = input("Search: ").lower().strip()
    if search_input:
        search_base = []
        if all_tasks:
            for task in all_tasks:
                for items in task.values():
                    if search_input in str(items).lower():
                        matches = f"Title: {task.get('title').capitalize()}\nDescription: {task.get('description').capitalize()}\nPriority: {task.get('priority').upper()}\nStatus: {task.get('status').capitalize()}\nDue date: {task.get('due_date')}\n"
                        search_base.append(matches)
                        break
                    
            if search_base:
                print("Matches")
                for number,matches in enumerate(search_base, start=1):
                    print(f"{number}. {matches}")
            else:
                print("Nothing was found for this particular search, Try something else!")

        else:
            print("Can't search, add task to search!")
            
    else:
        print("Can't search, search box is empty!")
        
        
def update_task():
    if all_tasks:
        view_tasks(all_tasks)
        
        try:
            prompt = int(input("Enter the serial number of the task you want to update: ").strip())
            if 0<prompt<=len(all_tasks):
                prop_input = input("Which property do you want to update\n1. Title\n2. Description\n3. Priority\n4. Status\n5. Due date\n> ").strip()
                if prop_input in ("1","title"):
                    title = input("Enter new title: ").strip().lower()
                    if title:
                        all_tasks[prompt - 1]["title"] = title
                        save_file()
                        print("Task's title has been updated successfully!")
                    else:
                        print("Can't update, Invalid title!")
                        
                elif prop_input in ("2", "description"):
                    desc = input("Enter new description: ").strip().lower()
                    if desc:
                        all_tasks[int(prompt)-1]["description"] = desc
                        save_file()
                        print("Task's description has been updated successfully!")
                    else:
                        print("Can't update, Invalid description!")
                        
                elif prop_input in ("3","priority"):
                    prior_list = ["high","medium","low"]
                    prior = int(input("Priority\n1. High\n2. Medium\n3. Low\nEnter priority serial number: ").strip())
                    if 1<=prior<=len(prior_list):
                        all_tasks[int(prompt)-1]["priority"] = prior_list[prior-1]
                        save_file()
                        print("Task's priority has been updated successfully!")
                    else:
                        print("Can't update, Invalid priority!")
               
                elif prop_input in ("4","status"):
                    status_list = ["pending","in_progress","completed"]
                    status = int(input("Status\n1. Pending\n2. In progress\n3. Completed\nEnter status serial number: ").strip())
                    if 1<=status<=len(status_list):
                        all_tasks[int(prompt)-1]["status"] = status_list[status-1]
                        save_file()
                        print("Task's status has been updated successfully!")
                    else:
                        print("Can't update, Invalid status serial number!")
                elif prop_input in ("5","duedate"):
                    due_date = input("Enter new Due date: ").strip()
                    if due_date:
                        all_tasks[int(prompt)-1]["due_date"] = due_date
                        save_file()
                        print("Due date has been updated successfully!")
                    else:
                        print("Can't update, Invalid Due date!")
                        
                else:
                    print("Invalid property!")
            
            else:
                print("Invalid serial number!")
                    
        except ValueError:
            print("Invalid command,Enter a number!")
    else:
        print("Can't update any property at the moment, Add a task!")
        
        
def task_stats():
    if all_tasks:
        status = {}
        total = len(all_tasks)
        
        for each_task in all_tasks:
            if each_task.get("status") not in status:
                status[each_task.get("status")] = 1
                
            else:
                status[each_task.get("status")] += 1
                
        if status:
            print(f"Total tasks: {total}")
            for key,value in status.items():
                print(f"{key}: {value}")
                
        else:
            print("There are no tasks at the moment!")
            
    else:
        print("There are no tasks in the database, add task to view task statistics")
        
        
def delete_task():
    if all_tasks:
        for number,task in enumerate(all_tasks,start=1):
            print(f"{number}. {task.get("title")}")
            
        try:
            prompt = int(input("Enter the serial number of the task you want to delete: ").strip())
            
            if 1<=prompt<=len(all_tasks):
                consent = input("Are you sure you want to delete the selected task? (yes/no):").lower().strip()
                if consent == "yes":
                    all_tasks.pop(prompt - 1)
                    save_file()
                    print("The task has been deleted!")
                    
                else:
                    print("Task was not deleted, you may continue with other operations!")
            else:
                print("Enter a valid serial number to delete!")
        
        except ValueError:
            print("Enter a number!")
        
    else:
         print("You cannot delete, add task to delete!")
         
         
def filter_task():
    def pending():
        pen_list = []
        for task in all_tasks:
            if task.get("status") == "pending":
                pen_list.append(task)
        
        if pen_list:       
            view_tasks(pen_list)
            
        else:
            print("There are no tasks with the status 'Pending'")
        
    
    def in_progress():
        prog = []
        for task in all_tasks:
            if task.get("status") == "in_progress":
                prog.append(task)
        
        if prog:        
            view_tasks(prog)
            
        else:
            print("There are no tasks with status 'In progress'")
            
    
    def completed():
        comp_list = []
        for task in all_tasks:
            if task.get("status") == "completed":
                comp_list.append(task)
                
        if comp_list:
            view_tasks(comp_list)
            
        else:
            print("There are no tasks with the status 'Completed'")
        
        
    if all_tasks:
        prompt = input("Filter by:\n1. Pending\n2. In progress\n3. Completed\n> ").replace(" ","").lower()
        if prompt in ("1","pending"):
            pending()
            
        elif prompt in ("2", "inprogress"):
            in_progress()
            
        elif prompt in ("3", "completed"):
            completed()
            
        else:
            print("Invalid command!")
    
        
print("===== TASK MANAGER =====")
while True:
    user_prompt = input("\n1. Add task\n2. View all tasks\n3. Search task\n4. Update task\n5. Task statistics\n6. Delete task\n7. Filter task\n8. Exit\n> ").replace(" ","").lower()
    
    if user_prompt in ("1","addtask"):
        add_task()
    
    elif user_prompt in ("2","viewalltasks"):
        view_tasks(all_tasks)
        
    elif user_prompt in ("3", "searchtask"):
        search_task()
        
    elif user_prompt in ("4","updatetask"):
        update_task()
        
    elif user_prompt in ("5","taskstatistics"):
        task_stats()
        
    elif user_prompt in ("6","deletetask"):
        delete_task()
        
    elif user_prompt in ("7", "filtertask"):
        filter_task()
        
    elif user_prompt in ("8","exit"):
        print("Exiting...")
        time.sleep(3)
        print("Exited!")
        break
        
    else:
        print("Invalid command!")