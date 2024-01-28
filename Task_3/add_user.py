import getpass
import codecs

def add_user(file_pass):

    with open(file_pass, "r") as file:
        lines = file.readlines()

    username = input("Enter your username: ")
    user_exists = any(line.split(":")[0] == username for line in lines)
    if user_exists:
        print("Error: Username already exists.")
        return

    name = input("Enter your Full name: ")
    password = getpass.getpass("Enter your password: ")
    # password = input("Enter your password: ")
    password = codecs.encode(password, "rot_13")

    # user_exists = any(line.split(":")[0] == username for line in lines)


    new_user = f"{username}:{name}:{password}\n"
    lines.append(new_user)

    with open(file_pass, "a") as new_file:
        new_file.write(new_user)

    print(f"User '{username}' added successfully.")

# add_user("passwd.txt")