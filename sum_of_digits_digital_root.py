def digital_root(n):
    result = sum(int(x) for x in str(n))
    return result if len(str(result)) == 1 else digital_root(result)