def paul(x):
    score = x.count('kata') * 5 + x.count('eating') + x.count('Petes kata') * 10
    if score < 40: return "Super happy!"
    elif score < 70: return "Happy!"
    elif score < 100: return "Sad!"
    else: return "Miserable!"
