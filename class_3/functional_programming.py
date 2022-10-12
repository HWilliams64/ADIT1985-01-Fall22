def call_that(func, arg_1, arg_2):
    """
    This is my function that calls the argument func passing in the arg_1 and arg_2
    """
    func(arg_1, arg_2)

def add(x, y):
    print(x+y)


def sub(x, y):
    print(x-y)


call_that(add, 1, 2)