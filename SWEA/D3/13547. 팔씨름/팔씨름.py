T=int(input()) #testcase
for i in range(T): #testcase 만큼 반복
    X=input() #문자열
    X2=list(X)
    if len(X2)==15:
        if X2.count('o')>=8:
            print('#%d YES'%(i+1))
        else:
            print('#%d NO'%(i+1))
    elif len(X2)<15:
        if X.count('x')>=8:
            print('#%d NO'%(i+1))
        else:
            print('#%d YES'%(i+1))            
