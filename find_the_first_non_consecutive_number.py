def first_non_consecutive(arr):
    for i, x in enumerate(arr):
        if i == len(arr)-1: return None
        if arr[i+1] - x > 1: return arr[i+1]
        