X=int(input())
T=set(list(map(int, input().split()))) #중복 제거
T2=list(T)
T2.sort()
print(*T2)