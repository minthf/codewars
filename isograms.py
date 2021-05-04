def is_isogram(string):
    return True if len(list(set(list(string.lower())))) == len(list(string.lower())) else False