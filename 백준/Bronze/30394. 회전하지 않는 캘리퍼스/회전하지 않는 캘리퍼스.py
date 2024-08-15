T=int(input()) # testcase
Y_lst=[]
'''
왜 X좌표는 고려하지 않는 건가?
캘리퍼스는 y축과 평행하게 세워져있고 날은 x축과 평행하게 놓여져있음
-> 위아래로만 움직여서 x축 방향으로의 거리 고려 X
'''
for i in range(T):
    X, Y=map(int, input().split()) 
    Y_lst.append(Y)
# 캘리퍼스가 측정한 거리 값을 출력 -> 가장 큰 값에서 가장 작은 값을 빼면 됨
print(max(Y_lst)-min(Y_lst))
