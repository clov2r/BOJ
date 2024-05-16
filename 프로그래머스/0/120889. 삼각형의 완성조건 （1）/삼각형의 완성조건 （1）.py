def solution(sides):
    a=max(sides)
    b=sum(sides)
    c=b-a #가장 긴 변을 제외한 다른 두 변의 길이
    if a<c:
        answer=1
        return answer
    elif a==2*c:
        answer=1
        return answer
    else:
        answer=2
        return answer