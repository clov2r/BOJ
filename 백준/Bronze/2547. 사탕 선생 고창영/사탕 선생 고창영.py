t=int(input()) #testcase
for i in range(t):
    input()
    x=int(input()) #사람 수 입력
    x_list=[] # 학생이 가져온 사탕의 수
    for j in range(x):
        x_list.append(int(input()))
    res=sum(x_list)
    if res%x==0: #모두에게 같은 사탕을 나눠줄 수 있는 경우
        print("YES")
    else:
        print("NO")
