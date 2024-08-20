N = int(input())
members = []

# 입력을 받아 리스트에 저장
for i in range(N):
    age, name = input().split()
    members.append((int(age), name, i))

# 나이 순으로 정렬하고, 나이가 같으면 입력 순서대로 정렬
members.sort(key=lambda x: (x[0], x[2]))

# 원하는 출력 형식으로 출력
for age, name, _ in members:
    print(age, name)
