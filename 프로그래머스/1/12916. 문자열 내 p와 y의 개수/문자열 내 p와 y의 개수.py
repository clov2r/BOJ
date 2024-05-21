def solution(s):
    s1=s.upper()
    s2=list(s1)
    A=s2.count('P')
    B=s2.count('Y')
    if A==B:
        return True
    else:
        return False
    return True