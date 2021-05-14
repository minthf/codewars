def digit(string):
    for chr in string:
        if chr.isdigit():
            return int(chr)
        
def order(sentence):
    return "" if (not sentence) else ' '.join(sorted(sentence.split(), key=digit))