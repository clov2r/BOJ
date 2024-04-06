N=int(input()) #설문 조사를 한 사람의 수
x=[] 
for _ in range(N):
    i=int(input())
    x.append(i) # 설문 조사의 값을 X 리스트에 넣음
lose=x.count(0)
win=x.count(1)
if(lose<win):
    print("Junhee is cute!")
elif(lose>win):
    print("Junhee is not cute!")
