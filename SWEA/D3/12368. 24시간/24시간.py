T=int(input()) #testcase 수를 입력
for i in range(T): #testcase만큼 반복
    X, Y=map(int, input().split()) #X시에서 Y시간이 지난 상황을 입력받음
    now=X+Y #현재 시간을 계산
    if X+Y==24: #24시간제 시계라 조건을 여러 개 나눔
        print('#%d'%(i+1), now%24)  # 24로 나눈 나머지를 출력 (0시부터 다시 시작)
    elif X+Y>24:
        print('#%d'%(i+1), now%24)  # 24로 나눈 나머지를 출력 (0시부터 다시 시작)
    else:
        print('#%d'%(i+1), now) #현재 시간 그대로 출력 