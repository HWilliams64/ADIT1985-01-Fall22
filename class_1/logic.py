"""
my_password = 'password123'

user_input = input('Please enter your password:')

my_string = "the dog jumped over"

is_correct = user_input not in my_string

print(f'Is "{user_input}" in "{my_string}"? {is_correct}')
"""


the_password = 'password123'

user_input = input('Please enter your password:')


if the_password == user_input:
    print('You have type the correct password!!!')
elif user_input.casefold() in the_password.casefold():
    print('Close but now quite right.')
else:
    print('You have typed the wrong password :(')