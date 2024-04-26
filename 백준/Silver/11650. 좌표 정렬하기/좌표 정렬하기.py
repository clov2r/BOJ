import sys
T = int(sys.stdin.readline().strip())  # testcase
X = []
for _ in range(T):
    X.append(list(map(int, sys.stdin.readline().split())))  # 2차원 리스트 입력
X2 = sorted(X)
for row in X2:
    print(*row)