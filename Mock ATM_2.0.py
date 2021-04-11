import random

database = {}

def init():
    

    print("Welcome to bankPY")
    
    haveAccount = int(input("Do you have account with us: 1 (yes) 2 (no) \n"))
        
    if(haveAccount == 1):
            
        login()
    elif(haveAccount == 2):
            
        register()
    else:
        print("You have selected invalid option")
        init()

def login():
    
    print("*** Login ***")

    accountNumberFromUser = int(input("What is your account number? \n"))
    password = input("What is your password \n")

    for accountNumber,userDetails in database.items():
        if(accountNumber == accountNumberFromUser):
            if(userDetails[3] == password):
                bankOperation(userDetails)   
    else:
        print("Invalid account or password, please try again")   
        login()


def register():

    print("*** Register ***")

    email = input("What is your email address? \n")
    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    password = input("create a password for yourself \n")

    accountNumber = generationAccountNumber()

    database[accountNumber] = [ first_name, last_name, email, password ]

    print("Your Account Has been created")
    print(" == ==== ====== ===== ===")
    print("Your account number is %d" % accountNumber)
    print("Make sure you can keep it safe")
    print(" == ==== ====== ===== ===")

    login()

def bankOperation(user):
    
    import datetime
    x = datetime.datetime.now()
    print(x)

    print("Welcome %s %s " % ( user[0], user[1] ) )
    
    selectedOption = int(input("What would you like to do? (1) deposit (2) withdrawal (3) Complaint (4) Exit \n"))

    if(selectedOption == 1):
            
        depositOperation()
    elif(selectedOption == 2):
            
        withdrawalOperation()
    elif(selectedOption == 3):
            
        complaint()
    elif(selectedOption == 4):
            
        exit()
    else:

        print("Invalid option selected")
        bankOperation(user)

def withdrawalOperation():
    print('You selected (2) withdrawal')
    input('How much would you like to withdraw? \n')
    print('Take your cash')
    anotherTransaction = int(input('Another transaction? (1) yes, or select any other number to exit \n'))

    if(anotherTransaction == 1):
        login()
    else:
        exit()


def depositOperation():
    print('You selected (1) desposit')
    currentBalance = input('How much would you like to deposit? \n')
    print('Your current balance is $ %s' % currentBalance)
    anotherTransaction = int(input('Another transaction? (1) yes, or select any other number to exit \n'))

    if(anotherTransaction == 1):
        login()
    else:
        exit()

def complaint():
    print('You selected (3) complaint')
    input('What issue will you like to report? \n')
    print('Thank you for contacting us')
    anotherTransaction = int(input('Another transaction? (1) yes, or select any other number to exit \n'))

    if(anotherTransaction == 1):
        login()
    else:
        exit()

def generationAccountNumber():

    return random.randrange(1111111111,9999999999)

def logout():
    login()

### ACTUAL BANKING SYSTEM ###

init()