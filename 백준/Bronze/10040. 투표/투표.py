N, M = map(int, input().split()) # N: 경기의 수, M: 위원의 수
x = [] # 경기를 개최하는데 필요한 비용 리스트
y = [] # 위원의 심사 기준 리스트
cnt = [0] * N # 경기에 대한 투표 수를 세기 위한 리스트를 0으로 초기화

# 경기를 개최하는데 필요한 비용을 입력
for i in range(N):
    x.append(int(input()))

# 각 위원의 심사 기준을 입력
for i in range(M):
    y.append(int(input()))

# 각 위원이 자신의 심사 기준에 따라 투표하는 과정
for j in range(M):
    for i in range(N):
        # 위원의 심사 기준이 경기의 비용보다 크거나 같은 경우 투표
        if y[j] >= x[i]:
            cnt[i] += 1
            break
print(cnt.index(max(cnt)) + 1) # 가장 많은 표를 획득한 경기의 번호를 출력 (1부터 시작)
