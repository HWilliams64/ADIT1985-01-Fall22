import random

matrix = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
]

def create_matrix(x, y):
    to_return = []
    for _ in range(x):
        row = []
        for _ in range(y):
            row.append(random.randint(1, 256))

        to_return.append(row)

    return to_return

def print_matrix(matrix):
    for row in matrix:
        for value in row:
            print(str(value).ljust(4, ' '), end='')
        print('')


print_matrix(create_matrix(4, 4))

for a, b, c, d in create_matrix(4, 4):
    print(a, b, c)
