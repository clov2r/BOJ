def solution(s):
    if len(s)%2==1:
        answer = s[len(s)//2]
        return answer
    else:
        answer=s[len(s)//2-1:len(s)//2+1]
        return answer