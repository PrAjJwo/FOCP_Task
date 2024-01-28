import codecs
import getpass

def del_user(file_pass):

    lines = []
    with open(file_pass, "r") as file:              # Read existing entries from the file
        for line in file:
            lines.append(line.strip())

    username = input("Enter your username: ")
    # password = input("Enter your password: ")
    password = getpass.getpass("Enter your password: ")
    password = codecs.encode(password, "rot_13")

    user_index = None
    for i in range(len(lines)):   # Check if the username exists
        if lines[i].split(":")[0] == username:
            user_index = i
            break

    # if user_index != None:
    if user_index is not None:    # Remove the user entry from the list
        lines.pop(user_index)

        with open(file_pass, "w") as updated_file:
            for line in lines:
                updated_file.write(line + "\n")

        print(f"User '{username}' deleted successfully.\n")
    else:
        print("Error: User not found.")

