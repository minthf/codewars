def sum_of_n(n):
    if n >= 0:
        return [sum([i for i in range(x+1)]) for x in range(n+1)]
    return [sum([i for i in range(0, x-1, -1)]) for x in range(0, n-1, -1)]