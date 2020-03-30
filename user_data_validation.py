# Container for holding all created user data called 'users'
users = {}

def createUser():
    # The extra .lower() method returns lowercased strings
    firstName = input("Enter first name: ").lower()
    lastName = input("Enter last name: ").lower()
    email = input("Enter email: ").lower()
    password = generatePassword(firstName, lastName)
    
    print(f"\nYour new password is '{password}'.\nIf you would like to adopt it, enter 'y' below, else enter 'n'. ")
    user_response = input("Your response: ")
    
    if user_response == 'n':
        password = choosePassword()
        users[firstName] = dict(firstname=firstName, lastname=lastName, email=email, password=password)
    else :
        users[firstName] = dict(firstname=firstName, lastname=lastName, email=email, password=password)
    print("\nYou have successfully created the user:")
    printUserCreated(firstName)
    # Go back to the beginning
    main()
        
def choosePassword():
    password = input("Enter your choice password: ")
    if len(password) < 7 :
        print("The password is weak. Password must be at least 7 characters long.")
        choosePassword()
    return password

def generatePassword(firstName, lastName):
    pre = firstName[:2]
    mid = lastName[-2:]
    post = generateRandomString()
    return pre + mid + post

def generateRandomString():
    import random
    additional_string = ''
    for i in range(5):
        # Combine letters of the English alphabeths to make a 5-long string 
        additional_string += chr(random.randrange(97, 122))     # chr() converts integer unicodes to their respective strings or characters
    return additional_string

def printUserCreated(user):
    # The extra method .title() returns strings starting with an uppercase letter
    firstname = user.title()
    lastname = users[user]['lastname'].title()
    email = users[user]['email']
    password = users[user]['password']
    print(f"Name: {firstname} {lastname}, email: {email}, password: {password}.")

# Execution starts with this function
def main():
    print("\nTo create a new user, Enter 1. Enter 0 to close the program\n")
    action = int(input("Action: "))
    if action == 1 : createUser()
    elif action == 0 :                                          # Terminates the program on the input of '0'
        print("\nHere are all the user created: ")
        for user in users: printUserCreated(user)               # Prints all user data from the collection before program termiantes
    else :                                                      # Invalid key causes the program to ask for an appropriate without terminating
        print("Not a valid action key! Try again.")
        main()

# Called to run the program from a command line interface
main()
