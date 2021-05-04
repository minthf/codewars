def count_positives_sum_negatives(arr):
    result = [0,0]
    for elem in arr:
        if elem > 0:
            result[0] += 1
        else:
            result[1] += elem
    return result if arr else []