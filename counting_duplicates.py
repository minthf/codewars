def duplicate_count(text):
    a = set([x for x in text.lower()])
    return sum([1 for x in a if text.lower().count(x) > 1])
     