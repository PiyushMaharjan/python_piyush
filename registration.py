# A simple dictionary to hold our registered user
# (We start with an empty database)
database = {}

def main():
    print("Welcome! Please choose an option:")
    print("1. Register a new account")
    print("2. Log in to an existing account")
    
    choice = input("Enter 1 or 2: ")
    
    if choice == "1":
        register_user()
    elif choice == "2":
        login_user()
    else:
        print("Invalid choice. Please run the program again and select 1 or 2.")

def register_user():
    print("\n--- Registration ---")
    username = input("Create a username: ")
    password = input("Create a password: ")
    
    # Store the username and password in our database
    database[username] = password
    print("Registration successful!")
    
    # Automatically ask them if they want to log in now
    print("\nWould you like to log in now?")
    answer = input("Type 'yes' or 'no': ")
    if answer == "yes":
        login_user()
    else:
        print("Goodbye!")

def login_user():
    print("\n--- Login ---")
    username = input("Username: ")
    password = input("Password: ")
    
    # Condition 1: Check if the username exists in our database
    if username in database:
        # Condition 2: Check if the password matches the one stored
        if database[username] == password:
            print(f"Success! Welcome back, {username}.")
        else:
            print("Incorrect password!")
            
    else:
        print("Username not found! You need to register first.")

# This calls the main function to start the program
main()