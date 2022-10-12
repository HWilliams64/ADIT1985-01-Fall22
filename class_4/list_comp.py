# [element_to_add for element_to_add in elements]
# for i in range(10)


my_list = []
for i in range(10):
    # i has be larger than 10 and even 
    if i > 10 or i % 2 == 0:
        my_list.append(i)

my_list = [i for i in range(10) if i > 10 or i % 2 == 0]