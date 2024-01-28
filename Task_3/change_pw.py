
import codecs
def change_password(file_pass):

    import getpass
    lines = []
    with open(file_pass, "rt") as file:
        # lines = file.readlines()
        for line in file:
            lines.append(line)

    username = input("Enter your username: ")
    # current_password = input("Enter your current password: ")
    current_password = getpass.getpass("Enter your current password: ")
    # current_password = codecs.encode(current_password, "rot_13")
    # updated_lines = []

    for i in range(len(lines)):
            stored_username = lines[i].split(":")[0]
            user_name_full = lines[i].split(":")[1]
            stored_encrypted_password = lines[i].split(":")[2]
            stored_password = codecs.decode(stored_encrypted_password.strip(), "rot_13")

            if stored_username == username:

                if current_password == stored_password:
                    new_password = input("Enter your new password: ")
                    new_password_confirm = input("Enter your new password again: ")

                    if new_password == new_password_confirm:  # Encrypt the new password using ROT-13
                        encrypted_new_password = codecs.encode(new_password, "rot_13")
                        lines[i] = f"{username}:{user_name_full}:{encrypted_new_password}\n"  # Update the password in the list

                        with open(file_pass, "w") as updated_file:  # Write the updated entries back to the file
                            updated_file.writelines(lines)

                        print("Password changed successfully.")
                        return
                    else:
                        print("Error: New passwords do not match.")
                        return

    print("Error: User not found or incorrect password.")


# change_password("passwd.txt")