T = int(input()) # testcase
for i in range(T):
    N, M = map(int, input().split())
    print('#%d'%(i+1), N+M)
