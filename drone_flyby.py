def fly_by(lamps, drone):
    return ''.join(['o' if x < len(drone) else 'x' for x in range(len(lamps))])