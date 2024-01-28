import codecs
import getpass

def login_user(file_pass):
    lines = []
    with open(file_pass, "r") as file:
        for line in file:
            lines.append(line.strip())

    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")
    # password = input("Enter your password: ")
    # password = codecs.encode(password, "rot_13")

    for line in lines:
        exiting_username, _, password_stored = line.split(":")
        if exiting_username == username:
            stored_password = codecs.decode(password_stored, "rot_13")
            if password == stored_password:
                print(f"Login successful for user '{username}'.")
                return
            else:
                print("Login failed: Incorrect password.")
                return

    print("Login failed: User not found.")