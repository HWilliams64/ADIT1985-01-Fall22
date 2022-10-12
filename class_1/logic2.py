# and   => * => multiply
# or    => + => add
# true  => 1
# false => 0
# PEMDAS => Order of operation

# 1 * (1 + 1)
#print(True and (True or True)) 

fruits = [ 'apple', 'orange', 'banana', 'orange', 'grapes']
count = 0
for fruit in fruits:
    if fruit.startswith('o'):
        count += 1
print(count)