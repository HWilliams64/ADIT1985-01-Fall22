import os
# / C:// -> Root directory


print(os.path.abspath('/'))
print(os.path.abspath('./heros.csv'))
print(os.path.abspath('../'))
print(os.path.abspath('../../'))
print(os.path.dirname(__file__))
# give you the parent file path of the current file os.path.dirname(__file__)

new_path = os.path.join(os.path.dirname(__file__))

if os.path.exists(new_path):
    print("It exist")

if os.path.isdir(new_path):
    print("It is a directory")

if os.path.isfile(new_path):
    print("It is a file")
