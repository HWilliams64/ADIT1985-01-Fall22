def fun_raise_exception():
    raise FileNotFoundError("This is my wonderful error")

def fun_c(v):
    for value in v:
        if value > 4:
            raise ValueError("The values must be less than 4")

def fun_b(v):
    fun_c(v)

def fun_a(v):
    fun_b(v)

fun_a([1, 2, 3, 4, 5])