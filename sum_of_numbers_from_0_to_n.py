def show_sequence(n):
    if n == 0:
        return '0=0'
    if n < 0:
        return f"{n}<0"
    arr = [str(x) for x in range(n+1)]
    return '+'.join(arr) + f" = {sum([int(x) for x in arr])}"