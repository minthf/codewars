def calculator(x,y,op):
    if not (str(x).isdigit() and str(y).isdigit()): return "unknown value"
    return {
        '+':x+y,
        '-':x-y,
        '*':x*y,
        '/':x/y,
    }.get(op, 'unknown value')
