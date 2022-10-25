from os import system
import sys
py_code = ""
with open('file_read.py') as file:
    for line in file:
        py_code += line

with open('file_read_2.py', 'w') as file:
    py_code = py_code.replace('file_read.py', 'file_write.py')
    file.write(py_code)

system('python file_read_2.py')
