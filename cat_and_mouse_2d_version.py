def cat_mouse(map_, moves):
    map_ = map_.split('\n')
    cat = []
    mouse = []
    for i, string in enumerate(map_):
        if string.find('C') >= 0:
            cat = [i,string.find('C')]
        if string.find('m') >= 0:
            mouse = [i,string.find('m')]
    if len(cat) == 0 or len(mouse) == 0:
        return 'boring without two animals'
    if abs(cat[0]-mouse[0]) + abs(cat[1]-mouse[1]) <= moves:
        return 'Caught!'
    return 'Escaped!'
    