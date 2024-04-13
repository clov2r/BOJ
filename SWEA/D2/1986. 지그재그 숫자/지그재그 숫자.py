T=int(input()) #testcase
for i in range(1, T+1):
    N=int(input()) #number
    res=0 #누적된 값
    for j in range(1, N+1):
        if(j%2==1): # 홀수면 더하기
            res+=j
        elif(j%2==0): # 짝수면 뺌
            res-=j
    print('#%d'%i, res)
