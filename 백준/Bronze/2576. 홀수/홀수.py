lst=[] #7개의 자연수를 받을 리스트
lst2=[]
for i in range(7):
    lst.append(int(input()))
    if lst[i] %2!=0:
        lst2.append(lst[i])
if len(lst2)==0: #홀수가 존재하지 않는 경우
    print(-1)
else:
    print(sum(lst2))
    print(min(lst2))

