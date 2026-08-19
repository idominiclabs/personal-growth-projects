task_database = []


def add_task(task):
    duplicate = False
    for item in task_database:
        if task.lower() == item.lower():
            duplicate = True
            break
    if not task.strip():
        print("Enter a valid character!!")
        
    elif duplicate:
        print("Task already exists!!")
        
    else:
        task_database.append(task)
        print("Task has been successfully added!!")


def view_tasks():
    print("\nTasks")
    for number,items in enumerate(task_database, start=1):
         print(f"{number}. {items}")
        
        
def search_task(task):
    matches = []
    for items in task_database:
        if task.lower() in items.lower():
            matches.append(items)
            
    return matches
    
    
def delete_task(task):
    if task == "":
        print("Enter a valid character!!")
        
    else:
        if task <= len(task_database):
            for item in task_database:
                if task_database.index(item)+1== task:
                    print(f"{item} has been deleted!")
                    task_database.remove(item)
                
                    view_tasks()
                
        else:
            print("Invalid task number")
                
        
def delete_all_tasks():
    consent = input("Are you sure you want to delete all tasks? (yes/no)").lower().strip()
    if consent == "yes":
        print("All tasks have been deleted, Add new task")
        task_database.clear()
        
    else:
        print("Tasks not deleted!")


print("Ω==================To-do Manager ==================Ω")
while True:
    user_prompt = input("\n1. Add task\n2. View tasks\n3. Search task\n4. Count tasks\n5. Delete task\n6. Delete all tasks\n7. Exit\n> ").replace(" ","").lower()

    if user_prompt in ("1","addtask"):
        prompt = input("Input task you wanna add: ").lstrip().rstrip()
        add_task(prompt)
    
    elif user_prompt in ("2","viewtasks"):
        if len(task_database) > 0:
            view_tasks()
        else:
            print("No task available!")
            
    elif user_prompt in ("3","searchtask"):
        prompt = input("Search task: ")
        if not prompt.strip():
            print("Enter a valid character!!")
            
        elif len(task_database) > 0:
            result = search_task(prompt)
            if result:
                print("Matches")
                for number,items in enumerate(result, start=1):
                    print(f"{number}. {items}")
                
            else:
                print("Task not found!!")
                    
        else:
           print("No task is available, Add task")
           
    elif user_prompt in ("4", "counttasks"):
        print(f"Total tasks available: {len(task_database)}")
        
    elif user_prompt in ("5","deletetask"):
        try:
            if len(task_database) > 0:
                view_tasks()
                prompt = int(input("Input task serial number: "))
                delete_task(prompt)
            
            else:
                print("Can't delete, No task available ")
                
        except ValueError:
            print("Input a number")
            
    elif user_prompt in ("6","deletealltasks"):
        if len(task_database) > 0:
            delete_all_tasks()
            
        else:
            print("No task available to delete!!")
            
    elif user_prompt in ("7", "exit"):
       print("See you later!")
       break
       
    else:
        print("Enter a valid character!!")