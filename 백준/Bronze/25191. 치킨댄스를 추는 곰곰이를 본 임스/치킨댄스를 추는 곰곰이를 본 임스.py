N=int(input()) #치킨집에 있는 치킨의 개수
A, B=map(int, input().split()) #콜라, 맥주
#치킨 1마리 먹을 때 콜라 2개 또는 맥주 1개 먹음
A_C=A//2 #콜라 마실 때 먹는 치킨의 개수
B_C=B #맥주 마실 때 먹는 치킨의 개수
res=A_C+B_C
if res>N: #치킨집에 있는 치킨의 개수보다 치킨을 많이 먹을 수 없음
    val=res-N
    res-=val
print(res)