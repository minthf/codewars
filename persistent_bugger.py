def persistence(n):
    count = 0
    while n > 9:
        multi = 1
        for i in range(len(str(n))):
            multi *= int(str(n)[i])
        count += 1
        n = multi
    return count