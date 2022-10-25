# file = open('example.txt', 'w')
# file.write('Hello world 2')
# file.close()


with open('example.txt', 'a') as file:
    while True:
        text = input("Please type something: ")
        if text:
            file.write(text+"\n")
            file.flush()
        else:
            break
