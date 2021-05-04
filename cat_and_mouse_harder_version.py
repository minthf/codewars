def cat_mouse(x,j):
    if x.find("D") == -1 or x.find("C") == -1 or x.find("m") == -1:
        return "boring without all three"
    mn = min(x.find('C'), x.find('m'))
    mx = max(x.find('C'), x.find('m'))
    if x[mn:mx].count('.') <= j:
        if x[mn:mx].find('D') == -1:
            return "Caught!"
        else: return "Protected!"
    else: return "Escaped!"