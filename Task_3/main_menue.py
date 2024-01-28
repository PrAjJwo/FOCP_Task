from change_pw import change_password
from login_user import login_user
from delete_user import del_user
from add_user import add_user
import sys

def main_menu():
    while True:
        print("1. Add User")
        print("2. Delete User")
        print("3. Change Password")
        print("4. Login")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_user("passwd.txt")
        elif choice == "2":
            del_user("passwd.txt")
        elif choice == "3":
            change_password("passwd.txt")
        elif choice == "4":
            login_user("passwd.txt")
        elif choice == "5":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


main_menu()