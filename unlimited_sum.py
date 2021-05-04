def sum(*args):
    summ = 0
    for arg in args:
        if isinstance(arg,int):
            summ += arg
    return summ
    