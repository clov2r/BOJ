W=[]
K=[]
for i in range(10):
    W.append(int(input()))
for t in range(10):
    K.append(int(input()))
W2=sorted(W)
K2=sorted(K)
print(sum(W2[-3:]), sum(K2[-3:]))
