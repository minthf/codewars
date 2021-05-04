def most_money(students):
    money = [x.fives*5 + x.tens*10 + x.twenties*20 for x in students]
    if len(set(money)) == 1 and len(money) != 1: return "all"
    return students[money.index(max(money))].name
    