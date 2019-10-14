from functools import partial
def my_function(m,n):
    print(m,n)
    print(m/n)

partfun = partial(my_function,n=100)


partfun(19)