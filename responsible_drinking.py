def hydrate(drink_string):
    water = sum([int(x) for x in drink_string.split() if x.isdigit()])
    return '1 glass of water' if water == 1 else f"{water} glasses of water"