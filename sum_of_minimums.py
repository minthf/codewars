def sum_of_minimums(numbers):
    sum = 0
    for array in numbers:
        sum += min(array)
    return sum

