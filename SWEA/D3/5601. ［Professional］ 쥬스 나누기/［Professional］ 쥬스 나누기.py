T = int(input()) # testcase
for i in range(T):
    N = int(input())
    print('#%d' %(i+1), end='')
    for t in range(N):
        if t == 0:
            print(' 1/%d' %N, end='') # 첫 번째 분수 출력
        else:
            print(' 1/%d' %N, end='') # 나머지 분수 출력
    print()  # 줄 바꿈
