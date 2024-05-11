for i in range(10):
    A=int(input())
    B, C=map(int, input().split())
    print('#%d'%(i+1), pow(B, C))
