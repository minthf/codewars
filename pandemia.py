def infected(s):
    all = sum([len(x) for x in s.split('X')])
    inf = sum([len(x) for x in s.split('X') if (x and int(x))])
    return inf * 100 /all if inf > 0 else 0
