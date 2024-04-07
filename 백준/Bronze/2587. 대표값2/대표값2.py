def solution(X):
    X.sort()
    return X[len(X)//2]
X=[]
for i in range(5):
    X.append(int(input()))
avg=int(sum(X)/len(X))
print(avg) # 평균값
print(solution(X)) #중앙값