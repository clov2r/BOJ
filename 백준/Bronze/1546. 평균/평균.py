N=int(input()) # N개의 정수
N_list=list(map(int, input().split())) # 최솟값 최댓값을 구하는 배열
M=max(N_list) # 최고점
X=[] #N_list의 수정본
for i in range(len(N_list)):
    X.append(N_list[i]/M*100)
res=sum(X)
print(res/len(X))