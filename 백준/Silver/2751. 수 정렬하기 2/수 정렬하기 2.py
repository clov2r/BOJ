import sys 
T = int(sys.stdin.readline())
X = []
for i in range(T):
    X.append(int(sys.stdin.readline().strip()))
X2 = sorted(X)
for i in range(T):
    print(X2[i])
