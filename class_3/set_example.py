list_1 = [1, 2, 3]
list_2 = [3, 2, 1]

def function():
    if len(list_1) != len(list_2):
        return ('Not the the same')


    for item_1 in list_1:
        if item_1 not in list_2:
            return ('They are not the same')

    return ('They are the same same')
