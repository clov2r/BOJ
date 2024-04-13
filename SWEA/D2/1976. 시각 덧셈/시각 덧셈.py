T=int(input()) #testcase
for i in range(1, T+1):
    A, B, C, D=map(int, input().split()) #시 분 시 분 입력
    Hour=A+C
    Min=B+D
    #예외처리 1<=A+C<=12 AND 0<=B+D<=59

    if Hour>12:
        Hour-=12
    if(Min==60):
        Hour+=1
    if(Min>60):
        Hour+=1
        Min-=60
    print('#%d'%i, Hour, Min)


