name = input('What is your name? \n')
allowedUsers = ['Seyi','Mike','Love']
allowedPassword = ['passwordSeyi','passwordMike','passwordLove']

if(name in allowedUsers):
    password = input('Your password? \n')
    userId = allowedUsers.index(name)
    
    while True:
        
        if(password == allowedPassword[userId]):

            import datetime
            x = datetime.datetime.now()
            print(x)

            print('Welcome %s' % name)
            print('These are the available options:')
            print('1. Withdrawal')
            print('2. Cash Deposit')
            print('3. Complaint')

            selectedOption = int(input('Please select an option:'))

            if(selectedOption == 1):
                print('You selected %s' % selectedOption)
                input('How much would you like to withdraw? \n')
                print('Take your cash')

            elif(selectedOption ==2):
                print('You selected %s' % selectedOption)
                currentBalance = input('How much would you like to deposit? \n')
                print('Your current balance is $ %s' % currentBalance)

            elif(selectedOption == 3):
                print('You selected %s' % selectedOption)
                input('What issue will you like to report? \n')
                print('Thank you for contacting us')

            else:
                print('Invalid Option selected, please try again')

        else:
            print('Password Incorrect, please try again')
            break

else:
    print('Name not found, please try again')   
    