N, X =map(int, input().split()) #N개의 수열 X보다 작은 수 출력
N_list=list(map(int, input().split())) #N개의 수열 생성
res=[] #N_list 안에 있는 요소들 중 X보다 작은 수만 저장하는 배열
for i in range(len(N_list)):
    if N_list[i]<X:
        res.append(N_list[i])
print(*res)