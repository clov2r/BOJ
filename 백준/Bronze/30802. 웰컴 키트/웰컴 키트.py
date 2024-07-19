import math
N=int(input()) #참가자 수
size_list=list(map(int, input().split())) #티셔츠 사이즈 별 신청자의 수
T, P=map(int, input().split()) #티셔츠와 펜의 묶음 수

# 각 사이즈별로 필요한 티셔츠 묶음 수 계산
shirt_bundles = [math.ceil(size / T) for size in size_list]

# 펜 묶음 수 계산
pen_bundles = N // P
remaining_pens = N % P

print(sum(shirt_bundles))
print(pen_bundles, remaining_pens)