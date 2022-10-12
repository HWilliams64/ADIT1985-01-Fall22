the_password = 'password123'
tries = 0
max_retries = 3

while tries < max_retries:
    tries +=1
    user_input = input('Please enter your password:')

    if the_password == user_input:
        print('You have type the correct password!!!')
        break # stops the while loop
    elif max_retries >= tries:
        print('You are locked out.')
    else:
        print('You have typed the wrong password :(')
