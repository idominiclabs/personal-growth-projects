import json

file_location = "vault.json"


try:
    with open(file_location, "r") as readfile:
        content = json.load(readfile)

except FileNotFoundError:
    with open(file_location, "w") as writefile:
        json.dump([], writefile)

    with open(file_location, "r") as readfile:
        content = json.load(readfile)


def saveToDb():
    with open(file_location, "w") as writefile:
        json.dump(content, writefile)


def logIn():
    print("LOGIN")
    username = input("Enter username: ").replace(" ","")
    password = input("Enter password: ").replace(" ","")

    for each in content:
        if username == each.get("user_name") and password == each.get("pass_word"):
            return each

        else:
            continue


def signUp():
    print("SignUp")
    username = input("Enter your unique username (username length should be within 4-10 characters): ").replace(" ","")
    password = input("Enter your strong password (username length should be within 6-13 characters): ").replace(" ","")
    pin = input("Enter your pin (numbers only, length=4): ").replace(" ","")

    if 4<=len(username)<=10 and 6<=len(password)<=13 and len(pin) == 4:
        duplicate = False

        for accounts in content:
            if username == accounts.get("user_name"):
                duplicate = True 
                break

        if duplicate:
            print("Account already exists, proceed to Login!")

        else:
            each_account = {
                "user_name": username,
                "pass_word": password,
                "pin": pin,
                "listOfAccounts": []
            }

            content.append(each_account)
            saveToDb()
            print("Your account has been created successfully!\nProceed to LogIn!")

    else:
        print("Character length for [username, paasword, pin] not adhered to, adhere to character rules to signup successfully")


def addAccount(user_exists):
    service = input("Enter service: ").lower().strip()
    name = input("Enter username or email: ").strip()
    acct_pass = input("Enter account password: ").strip()

    if service and name and acct_pass:
        user_account = {
            "service": service,
            "username/email": name,
            "password": acct_pass
        }
        if user_account not in user_exists.get("listOfAccounts"):
            user_exists.get("listOfAccounts").append(user_account)
            saveToDb()
            print("Account has been added successfully!")

        else:
            print("Couldn't add, account already exists!")

    else:
        print("Enter valid characters!")


def viewAccounts(user_exists):
    if user_exists.get("listOfAccounts"):
        print("All accounts")
        for number,accounts in enumerate(user_exists.get("listOfAccounts"), start=1):
            service = accounts.get("service")
            name = accounts.get("username/email")
            password = accounts.get("password")
            result = f"Service: {service}\nUsername/Email: {name}\nPassword: {password}"
            print(f"{number}. {result}\n")

    else:
        print("No account available, add account")


def search(user_exists, search_prompt):
    matches = []
    for accounts in user_exists.get("listOfAccounts"):
        service = accounts.get("service")
        name = accounts.get("username/email")
        if search_prompt.lower() in service.lower() or search_prompt.lower() in name.lower():
            matches.append(accounts)
        else:
            continue

    if matches:
        print("Search results")
        for number,items in enumerate(matches, start=1):
            form = f"Service: {items.get("service")}\nUsername/Email: {items.get("username/email")}\nPassword: {items.get("password")}"
            print(f"\n{number}. {form}")

    else:
        print(f"Nothing was found with '{search_prompt}'")


def deleteAccount(user_exists):
    try:
        serial_no = int(input("Enter the serial number of the account you want to delete: ").strip())
        if user_exists.get("listOfAccounts"):
            if 1<=serial_no <= len(user_exists.get("listOfAccounts")):
                user_exists.get("listOfAccounts").remove(user_exists.get("listOfAccounts")[serial_no-1])
                saveToDb()
                print("Account has been deleted successfully!")

            else:
                print("Enter a valid serial number!")

        else:
            print("Can't delete, no account is saved!")

    except ValueError:
        print("Enter a valid serial number!")


while True:
    prompt = input("\nCommands\n1. Login\n2. Signup\n3. Exit\n> ").lower().strip()

    if prompt in ("1", "login"):
        user_exists = logIn()

        if user_exists:
            while True:
                user_prompts = input("\nCommands\n1. Add new account\n2. View all accounts\n3. Search\n4. Delete an account\n5. Delete all accounts\n6. Log Out\n> ").lower().replace(" ","")

                if user_prompts in ("1", "addnewaccount"):
                    addAccount(user_exists)

                elif user_prompts in ("2", "viewallaccounts"):
                    pin = input("Enter your pin: ").replace(" ","")

                    if pin == user_exists.get("pin"):
                        viewAccounts(user_exists)
                    else:
                        print("Incorrect pin")

                elif user_prompts in ("3","search"):
                    if user_exists.get("listOfAccounts"):
                        search_prompt = input("Enter what you want to search for: ").replace(" ","")
                        if search_prompt:
                            pin = input("Enter your pin: ").replace(" ", "")
                            if pin == user_exists.get("pin"):
                                search(user_exists, search_prompt)
                            else:
                                print("Incorrect pin!")
                        else:
                            print("Invalid, Enter a valid character!")
                    else:
                        print("Can't search, they're no accounts!")
                        

                elif user_prompts in ("4", "deleteanaccount"):
                    viewAccounts(user_exists)
                    deleteAccount(user_exists)

                elif user_prompts in ("5", "deleteallaccounts"):
                    confirm = input("Are you sure you want to delete all accounts? (yes/no): ")
                    if confirm == "yes":
                        pin = input("Enter your pin: ").replace(" ","")
                        if pin == user_exists.get("pin"):
                            user_exists.get("listOfAccounts").clear()
                            saveToDb()
                            print("All accounts have been deleted successfully!")
                        else:
                            print("Incorrect pin!")
                    else:
                        continue

                elif user_prompts in ("6","logout"):
                    print("Logging out........\nLogged out!")
                    break

                else:
                    print("Enter a valid command!")
        else:
            print("User does not exist (Invalid username or password), SignUp!")

    elif prompt in ("2", "signup"):
        signUp()

    elif prompt in ("3", "exit"):
        break

    else:
        print("Enter a valid character!")