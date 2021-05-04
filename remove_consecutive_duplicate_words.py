def remove_consecutive_duplicates(s):
    new = []
    s = s.split()
    for i in range(len(s)-1):
        if s[i] != s[i+1]:
            new.append(s[i])
    if len(s) > 0: new.append(s[-1])
    return ' '.join(new)        
    