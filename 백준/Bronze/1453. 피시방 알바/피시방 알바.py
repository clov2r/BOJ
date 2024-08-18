N=int(input()) # 손님 수
N_list=list(map(int, input().split())) # 손님이 말하고 가는 번호
N_list2=list(set(N_list))
print(len(N_list)-len(N_list2))