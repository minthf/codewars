def number(bus_stops):
    sum = 0
    for people in bus_stops:
    	sum += people[0] - people[1]
    return sum