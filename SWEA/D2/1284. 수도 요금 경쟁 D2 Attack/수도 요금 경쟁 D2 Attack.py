T=int(input())
for i in range(T):
    #P = A사 리터당 요금 / Q = B사 기본 요금 / R = B사 월간사용량
    #S = B사 1리터 이상 사용시 리터당 요금 / W = 종민이 월간 사용량
    P,Q,R,S,W=map(int, input().split())
    A=P*W # A사 수도요금 계산
    D=W-R
    if (W>=R): #종민이가 이번달 사용량이 좀 많을 때
        B=(S*D)+Q #B사 수도요금 계산
        if(A>B):
            print('#%d' %(i+1), B)
        elif(A<B):
            print('#%d' %(i+1), A)
    elif(W<R): #종민이가 이번달 사용량이 적을 때
        if(A<Q):
            print('#%d' %(i+1), A)
        elif(A>Q):
            print('#%d' %(i+1), Q)
