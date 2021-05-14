def solution(s):
    return ''.join([x if x.islower() else f' {x}' for x in s])