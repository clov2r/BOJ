N, M= map(int, input().split()) #행렬의 크기 입력 받음
list1=[] #행렬 1
list2=[] #행렬 2
for i in range(N): #행렬 1 입력 받음
    list1.append(list(map(int, input().split())))
for j in range(N): #행렬 2 입력 받음
    list2.append(list(map(int, input().split())))
for x in range(N): #행렬 1과 행렬 2의 덧셈
    for y in range(M):
        print(list1[x][y]+list2[x][y], end=' ')
    print()