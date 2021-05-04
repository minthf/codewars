def declare_winner(fighter1, fighter2, first_attacker):
    i = 0
    if first_attacker == fighter1.name:
        fighter2.health -= fighter1.damage_per_attack
        i = 1
    if first_attacker == fighter2.name:
        fighter1.health -= fighter2.damage_per_attack
    while True:
        if fighter1.health <= 0:
            return fighter2.name
        if fighter2.health <= 0:
            return fighter1.name
        if i % 2 == 0:
            fighter2.health -= fighter1.damage_per_attack
        else:
            fighter1.health -= fighter2.damage_per_attack
        i += 1
            
            