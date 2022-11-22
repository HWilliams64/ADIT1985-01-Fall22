def fun_raise_exception():
    raise FileNotFoundError("This is my wonderful error")

def fun_c():
    fun_raise_exception()
    return 7

def fun_b():
    fun_c()

def fun_a():
    fun_b()

fun_a()