def find_it(seq):
    for elem in set(seq):
        if (seq.count(elem)%2 != 0):
            return elem
