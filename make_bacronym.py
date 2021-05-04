def make_backronym(acronym):
    return ' '.join([dictionary[x.upper()] for x in acronym])
