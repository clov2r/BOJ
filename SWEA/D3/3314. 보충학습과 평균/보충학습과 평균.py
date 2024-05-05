T=int(input()) #testcase
for i in range(T):
    X=list(map(int, input().split())) #학생들 점수
    for j in range(len(X)):
        if X[j]<40:
            X[j]=40
    avg=sum(X)//5
    print('#%d'%(i+1), avg)