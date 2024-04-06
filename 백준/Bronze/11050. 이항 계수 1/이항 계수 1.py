N, K=map(int, input().split())
C=N-K
X=1
Y=1
Z=1
for i in range(1, N+1):
    X *= i # 분모
for j in range(1, K+1):
    Y *= j # 분자
for d in range(1, C+1):
    Z *= d # 분자
print(int(X/(Y*Z)))
