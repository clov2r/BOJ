N, M=map(int, input().split()) #N과 M(목표값)을 입력 받음
N_list=list(map(int, input().split())) #N장 뽑힌 카드 리스트
tot=[] #N_list에서 카드 3장의 합을 보관할 리스트
tot_maxnum=-2147000000 #최댓값을 저장할 변수 초기화
for i in range(1, N): #N_list에서 세 장의 카드를 고르기 위한 반복문
    for j in range(i+1, N):
        for k in range(j+1, N):
            tot.append(N_list[i]+N_list[j]+N_list[k]) #카드 세 장의 합을 tot리스트에 추가
for i in range(len(tot)): #tot 리스트를 순회하면서 M보다 작거나 같은 값 중 최댓값을 찾는 반복문
    if tot[i]<=M:
        if tot[i]>tot_maxnum: #현재 값이 최댓값보다 크면 최댓값 갱신
            tot_maxnum=tot[i]
print(tot_maxnum)