import sys
A, B = map(int, sys.stdin.readline().split())  # 집합 A_list, B_list의 원소 개수
A_list = list(map(int, sys.stdin.readline().split()))  # 앞에 입력한 원소 개수대로 입력 받는 집합 A_list
B_list = list(map(int, sys.stdin.readline().split()))  # 앞에 입력한 원소 개수대로 입력 받는 집합 B_list
C = set(A_list) - set(B_list)  # A_list에만 있고 B_list에는 없는 요소들의 집합을 구함
C1 = set(B_list) - set(A_list)  # B_list에만 있고 A_list에는 없는 요소들의 집합을 구함
print(len(C) + len(C1))  # 차집합의 개수 출력