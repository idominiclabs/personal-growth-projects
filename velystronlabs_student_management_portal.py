student_database = []

def add_student():
    student_name = input("Input student name: ").strip()
    duplicate = False
     
    for student in student_database:
        if student.lower() == student_name.lower():
           duplicate = True
           break
            
             
    if student_name == "":
         print("Enter a valid name!!")
        
    elif duplicate:
        print("Student already exist")
        
    else:
        print(f"{student_name} has been added successfully!!")
        return student_name
        
        
def view_students():
    if student_database:
            for number,student in enumerate(student_database, start=1):
                print(f"{number}. {student}")
    else:
            print("No student in database")

        
def delete_student():
    student = input("Input Student name: ").strip()
    for students in student_database:
        if student.lower() == students.lower():
            student_database.remove(students)
            
            print(f"{student} has been removed from the student's database!!")
            view_students()
            return
            
    print("Can't delete, Student not found in student database")
        

def search(studentName):
    matches = []
    for student in student_database:
        if studentName.lower() in student.lower():
            matches.append(student)
       
    return matches
        

print("======= Velystronlabs Student Management Portal ========")

while True:
    request = input("\n1. Add student\n2. View students\n3. Search student\n4. Delete student\n5. Student count\n6. Delete student database\n7. Exit\n> ").replace(" ","").lower()
    
    if request in ("addstudent", "1"):
        name = add_student()
        if name is not None:
            student_database.append(name)
    
    elif request in ("viewstudents", "2"):
        view_students()
        
    elif request in ("searchstudent", "3"):
        studentName = input("Input Student's name: ")
        output = search(studentName)
        if output:
            for number,name in enumerate(output, start=1):
                print(number, name)
                
        else:
            print("Student not found, Student is not in the students database")
            
    elif request in ("deletestudent", "4"):
        delete_student()
        
    elif request in ("studentcount", "5"):
        student_count = len(student_database)
        print(student_count)
        
    elif request in ("deletestudentdatabase", "6"):
        if student_database:
            consent = input("Are you sure you want to delete the student database? (yes/no): ").lower().strip()
          
            if consent == "":
                 print("Enter a valid command")
            elif consent == "yes":
                 student_database.clear()

                 print("Student database deleted successfully!!")
                    
            else:
                 print("Database not deleted")
                    
        
        else:
            print("Can't delete, Student database is empty")
    
    elif request in ("exit", "7"):
        break
        
    else:
        print("Invalid Command")