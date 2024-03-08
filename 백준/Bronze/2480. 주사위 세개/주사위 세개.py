x, y, z = map(int, input().split())  # 입력 받기 및 정수 변환을 한 줄로 간소화

# 모두 같은 경우
if x == y == z:
    print(10000 + x * 1000)
# 두 개만 같은 경우
elif x == y or y == z or x == z:
    if x == y or x == z:
        print(1000 + x * 100)
    else:  # y == z
        print(1000 + y * 100)
# 모두 다른 경우
else:
    print(max(x, y, z) * 100)  # 가장 큰 수에 대해 계산
