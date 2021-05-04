def has_unique_chars(string):
    arr = [x for x in string]
    return True if sorted(arr) == sorted(list(set(arr))) else False

