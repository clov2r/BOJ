N, K=map(int, input().split()) #자연수 N / N의 약수들 중 K번째로 작은 수
X=[] #약수 리스트
for i in range(N):
    if N%(i+1)==0: #i+1로 나뉘어질 때 == 약수 -> 약수 리스트에 추가됨
        X.append(i+1)
if len(X)<K:
    print(0)
else:
    print(X[K-1])
