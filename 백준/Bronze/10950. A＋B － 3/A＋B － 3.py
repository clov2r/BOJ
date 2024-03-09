n = input()
n = int(n)
for _ in range(n):  # _는 반복에 사용되지 않는 변수임을 나타냅니다.
    a, b = input().split()
    a = int(a)
    b = int(b)
    print(a + b)
