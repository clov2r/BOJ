T=int(input()) #전체 테스트 케이스의 수
for i in range(T):
    X, Y=map(int, input().split()) #구구단 입력 받는 칸
    if X >= 10 and Y>=10: #1이상 9 이하의 자연수만 곱셈할 수 있음 나머지는 -1 처리
        print('#%d'%(i+1), -1)
    elif X>=10 and Y<=10:
        print('#%d'%(i+1), -1)
    elif X<=10 and Y>=10:
        print('#%d'%(i+1), -1)
    else:
        print('#%d'%(i+1), X*Y)