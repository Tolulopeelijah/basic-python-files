accounts = {'Elijah':'1223334444'}
def validator():
    global accounts
    while True:
        choice = input('\n what will you like to be welcome to: ? (Log in), (Sign up), (request_password)')

        if choice == 'Log in':
            username = input('pls, enter your username: ')
            if username in accounts:
                password = input('pls, enter your password' )
                if accounts[username] == password:
                    print('Access granted')
                    break
                else:
                    while True:
                        print('incorrect password \n will you like to reset your password? (Yes), (No), (Try again)')
                        rsttst = input('')
                        if rsttst == 'Yes':
                            password = input('pls, enter a new password:   ')
                            password2 = input('pls, enter the password again: ')
                            if password == password2:
                                accounts[username] = password
                            else:   
                                print('password don\'t match')
                        elif rsttst == 'No':
                            print('thanks for trying...bye')
                            break
                        elif rsttst == 'Try again':
                            rsttst = input('try again: ')
                            if accounts[username] == rsttst:
                                print('Access granted')
                                break
                            
                            else:
                                print('incorrect password')
                    else:
                        print('error input')
            else:
                print('pls, {} have no account, \n you are suggested to check the spelling and text case of \
the username, or create an account'.format(username))
        elif choice == 'Sign up':
            username = input('pls, enter a username: ')
            password = input('pls, enter a password: ')
            accounts[username] = password
            
        elif choice == 'request_password':
            username = input('enter your username ')
            if username in accounts:
                print('your password is ', accounts[username])
            else: print('gerrout, you no get shishi account for here')
        else:
            print('invalid input')
