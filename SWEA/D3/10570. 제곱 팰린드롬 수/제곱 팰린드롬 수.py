T=int(input()) #testcase
for i in range(T): #testcase 만큼 반복
    X, Y=map(int, input().split())
    res=[] # 1 4 9 121 484
    for j in range(X, Y+1):
        res.append(j)
    A=res.count(1)
    B=res.count(4)
    C=res.count(9)
    D=res.count(121)
    E=res.count(484)
    print('#%d'%(i+1), A+B+C+D+E)