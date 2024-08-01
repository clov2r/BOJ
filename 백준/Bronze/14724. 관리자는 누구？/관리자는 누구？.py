N=int(input())
#2차원 배열은 1차원 배열 입력 받기에서 for문을 추가하면 됨
#1차원 배열 입력 받기 list(map(int, input().split()))
N_list=[list(map(int, input().split())) for i in range(9)]
# 값 하나씩 탐색하여 최댓값을 찾는다
max_value=0
row=0
col=0
for i in range(9):
    for j in range(N):
        if N_list[i][j]>=max_value:
            max_value=N_list[i][j]
            row=i+1
            col=j+1
if row==1:
    print('PROBRAIN')
elif row==2:
    print('GROW')
elif row==3:
    print('ARGOS')
elif row==4:
    print('ADMIN')
elif row==5:
    print('ANT')
elif row==6:
    print('MOTION')
elif row==7:
    print('SPG')
elif row==8:
    print('COMON')
elif row==9:
    print('ALMIGHTY')

