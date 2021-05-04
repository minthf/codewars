def remove_every_other(my_list):
    removed = []
    for i in range(len(my_list)):
        if i%2 == 0:
            removed.append(my_list[i])
    return removed
