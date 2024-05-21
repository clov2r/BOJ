def solution(numbers):
    ans = []
    num=sorted(numbers)
    num2=[0,1,2,3,4,5,6,7,8,9]
    for i in num2:
        if i not in num:
            ans.append(i)
    answer=sum(ans)
    return answer