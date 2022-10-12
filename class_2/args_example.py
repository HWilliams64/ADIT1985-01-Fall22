def args_example(*args):
    print(args[0], args[2])

    for arg in args:
        print(arg)


#args_example(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)


def kwargs_example(**kwargs):
    print(kwargs['a'], kwargs['b'])


kwargs_example(a=1, b=2, c=3, d=4, e=5, f=6, g=7, h=8, i=9, j=10, k=11, l=12)