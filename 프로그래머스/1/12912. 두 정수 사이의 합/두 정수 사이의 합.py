def solution(a, b):
    x=[]
    if a>b:
        for i in range(b, a+1):
            x.append(i)
        answer=sum(x)
        return answer
    elif a<b:
        for i in range(a, b+1):
            x.append(i)
        answer=sum(x)
        return answer
    else:
        answer=a
        return answer