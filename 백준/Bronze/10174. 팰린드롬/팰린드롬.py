T=int(input()) #testcase
for i in range(T): #testcase 만큼 반복
    X=str(input()) #양수의 개수 N
    X2=list(X.upper())
    if X2[::-1]==X2:
        print('Yes')
    else:
        print('No')
