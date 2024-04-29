X=int(input())
T=[]
for i in range(X):
    T.append(int(input()))
T.sort()
print(*T, sep='\n')