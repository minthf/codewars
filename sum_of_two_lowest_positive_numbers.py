def sum_two_smallest_numbers(numbers):
    positive = sorted([x for x in numbers if x > 0])
    return positive[0]+positive[1]