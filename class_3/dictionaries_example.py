database = {
    "williayh": {
        "name": "Harris Williams", 
        "password": "password456", 
        "failed_login_attempts": 0,
        "access_times" : []
        },
    "qia": {
        "name": "Aisling Qi", 
        "password": "password789", 
        "failed_login_attempts": 0,
        "access_times": []
        },
    "cavallaj" : {
        "name": "Jason Cavallari", 
        "password": "password123", 
        "failed_login_attempts": 0,
        "access_times": []
        }
}

database["goetzk"] = 'Ken Goetz'



username = input('What is your username: ')

user_info = database.get(username, None)

if not user_info:
    print('Username not found')
else:
    password_actual = user_info['password']
    user_inputted_password = input("Please type your password: ")

    if password_actual == user_inputted_password:
        print(f"Hello {user_info['name']}")
        user_info['failed_login_attempts'] = 0
    else:
        print("The username and password do not match")
        user_info['failed_login_attempts'] += 1
