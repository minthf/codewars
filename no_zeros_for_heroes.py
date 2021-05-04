def no_boring_zeros(n):
    return n if str(n)[-1] != '0' or n == 0 else no_boring_zeros(int(str(n)[:-1]))