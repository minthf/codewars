def accum(s):
    return '-'.join([s[x].upper() + x * s[x].lower() for x in range(len(s))])
