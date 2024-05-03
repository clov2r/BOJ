T = int(input())  # 테스트케이스 수를 입력받음
for i in range(T):  # 테스트케이스 수만큼 반복
    X, Y, Z = map(int, input().split())  # 일주일에 X분 이상, Y분 이하 운동하는 경우와 이번 주에 운동한 시간을 입력받음
    if X<=Z<=Y: 
        print('#%d' %(i+1), 0)  # 적절한 운동량을 유지하고 있는 경우
    elif Z<X:
        print('#%d' %(i+1), X-Z)  # 목표 운동량에 미달하는 경우 추가로 몇 분 더 운동해야 하는지 출력
    else:
        print('#%d' %(i+1), -1)  # 너무 많은 운동을 한 경우 -1 출력