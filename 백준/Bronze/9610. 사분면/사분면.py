T=int(input()) #testcase
Q1, Q2, Q3, Q4, AXIS=0,0,0,0,0 # 사분면과 중심선 초기화
for i in range(T): #testcase만큼 반복
    x,y=map(int, input().split()) #좌표 입력
    #각 좌표가 0을 기준으로 사분면에 어디 속하는지 조건 돌림
    if x >0 and y>0:
        Q1+=1
    elif x<0 and y<0:
        Q3+=1
    elif x>0 and y<0:
        Q4+=1
    elif x<0 and y>0:
        Q2+=1
    elif x==0 or y==0:
        AXIS+=1
#출력
print('Q1:',Q1)
print('Q2:',Q2)
print('Q3:',Q3)
print('Q4:',Q4)
print('AXIS:',AXIS)

