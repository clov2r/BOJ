T = int(input()) # testcase
for i in range(T):
    X=int(input())
    if X%2==0:
        print('#%d'%(i+1), 'Even')
    else:
        print('#%d'%(i+1), 'Odd')
