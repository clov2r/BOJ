T = int(input()) # testcase
for i in range(T):
    X, Y, Z=map(int, input().split()) #사각형 변의 길이
    res=0 #나머지 한 변의 길이
    if X==Y==Z: #정사각형인 경우
        res=X
        print('#%d'%(i+1), res)
    elif X==Y:
        res=Z
        print('#%d'%(i+1), res)
    elif X==Z:
        res=Y
        print('#%d'%(i+1), res)
    elif Y==Z:
        res=X
        print('#%d'%(i+1), res)