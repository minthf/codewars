def draw_stairs(n):
    return ''.join([' '*i +'I\n' for i in range(n)][:-1]+[(n-1)*' '+'I'])
    