def max_sum_between_two_negatives(arr):
    max = 0
    sum = 0
    flag = False
    count = 0
    for el in arr:
        if el < 0:
            count += 1
            if flag:
                if max < sum: max = sum
                sum = 0
            else:
                flag = True
        else:
            if flag:
                sum += el
    if count <= 1: return -1
    return max
                