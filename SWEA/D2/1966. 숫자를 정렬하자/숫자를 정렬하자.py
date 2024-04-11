T=int(input())
for i in range(T):
    N=int(input()) # list 길이
    X = list(map(int, input().split()))
    X1=sorted(X)
    print('#%d'%(i+1),*X1)