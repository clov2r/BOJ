import sys
from collections import defaultdict

input = sys.stdin.readline  # 표준 입력을 빠르게 받기 위해 readline 사용

# 걸그룹 수(N)와 문제 수(M) 입력 받기
N, M = map(int, input().split())

# 그룹명과 멤버를 저장할 딕셔너리 생성
li = defaultdict(list)

# N개의 걸그룹 정보를 입력받아 딕셔너리에 저장
for _ in range(N):
    group = input().rstrip()  # 걸그룹 이름
    num = int(input())  # 걸그룹 멤버 수
    for _ in range(num):
        name = input().rstrip()  # 멤버 이름
        li[group].append(name)  # 걸그룹에 멤버 추가

# 딕셔너리를 일반 딕셔너리로 변환
li = dict(li)

# M개의 퀴즈를 처리
for _ in range(M):
    quiz_name = input().rstrip()  # 퀴즈의 이름 (걸그룹 이름 또는 멤버 이름)
    quiz_num = int(input())  # 퀴즈의 종류 (0: 팀명 주어짐, 1: 멤버명 주어짐)

    if quiz_num == 1:
        # 멤버 이름이 주어진 경우 해당 멤버가 속한 팀 이름 출력
        for key, values in li.items():
            if quiz_name in values:
                print(key)
                break
    elif quiz_num == 0:
        # 팀 이름이 주어진 경우 해당 팀의 멤버들을 사전순으로 출력
        if quiz_name in li:
            for member in sorted(li[quiz_name]):
                print(member)