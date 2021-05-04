def make_acronym(phrase):
    if isinstance(phrase,str):
        if any(map(str.isdigit, phrase)):
            return "Not letters"
        return ''.join([x[0].upper() for x in phrase.split()])
    else:
        return "Not a string"