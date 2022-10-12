import random



my_list = [random.randint(0, 100) for _ in range(10)]


def key(value):

    # this is even
    if value % 2 == 0:
        value -= 100 
    else:
        value += 100
    return value


my_list.sort(key = key)
print(my_list)