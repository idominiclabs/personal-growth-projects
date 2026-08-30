import json as js
import random as rd

file_path = "student_database.json"

try:
    with open(file_path, "r") as r_file:
        file_content = js.load(r_file)

except FileNotFoundError:
    print("Student database does not exist!")
    print("Creating student database...........")
    with open(file_path, "w") as w_file:
        js.dump([], w_file)

    with open(file_path, "r") as r_file:
        file_content = js.load(r_file)

    print("Student database created successfully, add a student!!!")


def add_student(first_name, last_name, department, level):
    duplicate = False

    for student in file_content:
        db_firstname = student.get("firstname")
        db_lastname = student.get("lastname")
        db_dep = student.get("department")
        db_level = student.get("level")
        
        if db_firstname == first_name and db_lastname == last_name and db_dep == department and db_level == level:
            duplicate = True
            break

    if duplicate:
        print("Student already exists!")

    else:
        student_id = f"FUT{rd.randint(0,9)}{rd.randint(0,9)}{rd.randint(0,9)}"
        for student in file_content:
            if student.get("student_id") == student_id:
                student_id = f"FUT{rd.randint(0,9)}{rd.randint(0,9)}{rd.randint(0,9)}"

        each_student = {
            "firstname": first_name,
            "lastname": last_name,
            "department": department,
            "level": level,
            "student_id": student_id
        }

        file_content.append(each_student)

        with open(file_path, "w") as w_file:
            js.dump(file_content, w_file)

        print(f"{first_name.capitalize()} {last_name.capitalize()} has been added successfully!!!")


def view_students():
    temp_data = []
    if file_content:
        for student in file_content:
            stud = f"Firstname: {student.get("firstname").capitalize()}\nLastname: {student.get("lastname").title()}\nDepartment: {student.get("department").upper()}\nLevel: {student.get("level")}\nStudent ID: {student.get("student_id")}"
            temp_data.append(stud)

    return temp_data
        

def student_count():
    if file_content:
        print("Student count:", len(file_content))

    else:
        print("Student database is empty!")


def search(any_param):
    temp_data = []
    for students in file_content:
        for items in students.values():
            if any_param in items.lower():
                stud = f"Firstname: {students.get("firstname").title()}\nLastname: {students.get("lastname").title()}\nDepartment: {students.get("department").upper()}\nLevel: {students.get("level")}\nStudent ID: {students.get("student_id")}"
                if stud not in temp_data:
                    temp_data.append(stud)

    return temp_data


def edit_student():
    result = view_students()
    if result:
        print("All Students")
        for number,items in enumerate(result, start=1):
            print(f"{number}. {items}\n")

        try:
            serial_no = int(input("Enter student serial number to edit: ").strip())
            if 1 <= serial_no <= len(file_content):
                parameter = input("What do you want to edit? (Firstname/Lastname/Department/Level): ").lower().strip()
                if parameter in ("firstname","lastname","department","level"):
                    parameter_value = input(f"Enter new {parameter.title()}: ").strip().lower()
                    file_content[serial_no - 1].update({parameter: parameter_value})

                    with open(file_path, "w") as w_file:
                        js.dump(file_content, w_file)

                    print(f"Student's {parameter} has been editted successfully!!!")

                else:
                    print("Invalid parameter!")

            else:
                print("Enter a valid serial number!")

        except ValueError:
            print("Enter a valid number")
        
    else:
        print("Student database is empty, add student to view!")
            


def delete_student(serial):
    if serial <= len(file_content):
        file_content.remove(file_content[serial - 1])
        with open(file_path, "w") as w_file:
            js.dump(file_content, w_file)

        print("Student has been deleted from students database!!!")

    else:
        print("Invalid serial number!")


def delete_all_students(confirmation_prompt):
    if confirmation_prompt == "yes":
        file_content.clear()
        with open(file_path, "w") as w_file:
            js.dump(file_content, w_file)
        print("All students have been deleted!!!")

    else:
        print("Operation cancelled, no student was deleted!")


print("==========Velystronlabs Student Management Portal v1.02==========")

while True:
    user_prompt = input("\nCommands\n1. Add student\n2. View all students\n3. Student count\n4. Search\n5. Edit student record\n6. Delete a student\n7. Delete all students\n8. Exit\n> ").lower().replace(" ","")

    if user_prompt in ("1", "addstudent"):
        firstName = input("Enter Firstname: ").lower().strip()
        lastName = input("Enter Lastname: ").lower().strip()
        department = input("Enter Department (e.g MCE, CPE, TME etc): ").upper().strip()
        level = input("Enter Level (e.g 100, 200 etc): ").strip()

        if firstName and lastName and department and level:
            add_student(firstName, lastName, department, level)

        else:
            print("Fill in all the required details!")

    elif user_prompt in ("2", "viewallstudents"):
        result = view_students()
        if result:
            print("All Students")
            for number,items in enumerate(result, start=1):
                print(f"\n{number}. {items}")

        else:
            print("Student database is empty, add student to view!")

    elif user_prompt in ("3", "studentcount"):
        student_count()

    elif user_prompt in ("4", "search"):
        search_char = input("Search: ").lower().strip()
        if search_char:
            matches = search(search_char)
            if matches:
                for number,each in enumerate(matches, start=1):
                    print(f"\n{number}. {each}")

            else:
                print(f"Student with {search_char} not found!")

        else:
            print("Enter valid characters!")

    elif user_prompt in ("5","editstudentrecord"):
        edit_student()

    elif user_prompt in ("6", "deleteastudent"):
        view_students()
        try:
            serial_no = int(input("Enter Student's serial number: ").strip())
            if serial_no >= 1 and serial_no <= len(file_content):
                delete_student(serial_no)
            else:
                print("Invalid serial number")

        except ValueError:
            print("Invalid character, enter a serial number from the list!")

    elif user_prompt in ("7", "deleteallstudents"):
        approval = input("Are you sure you want to delete all students? (yes/no): ").lower().strip()
        delete_all_students(approval)

    elif user_prompt in ("8", "exit"):
        print("Exiting.........")
        print("Exited, see you next time :)")
        break

    else:
        print("Invalid command, choose from the list of commands!")