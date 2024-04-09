def MID(X):
    X.sort()
    return(X[len(X)//2])
X=[]
for i in range(5):
    X.append(int(input()))

#평균
AVG=int(sum(X)/len(X))
print(AVG)
#중앙값
print(MID(X))
