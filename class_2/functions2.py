import hashlib

#f(x) = f(x)+1
# f(4) = 
def check_password(password_hash, inputted_password):
    in_hash = hashlib.sha256(inputted_password.encode("utf-8")).hexdigest()
    return password_hash == in_hash

def get_password(max_tries=3, tries=1):
    hash_password = hashlib.sha256('password'.encode("utf-8")).hexdigest()

    inputted_password = input("Please type your password:")

    if check_password(hash_password, inputted_password):
        print("You typed in the correct password")
    elif tries >= max_tries:
        print("You are locked out")
    else:
        print('That was the wrong password')
        get_password(tries=tries+1)


get_password()
