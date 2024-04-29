T = int(input())  # testcase
X = []
for _ in range(T):
    X.append(list(map(int, input().split())))  # 2차원 리스트 입력
X.sort(key=lambda x: (x[1], x[0]))  # y좌표 기준으로 정렬 후, y좌표가 같으면 x좌표 기준으로 정렬
for row in X:
    print(*row)
