import math
p = math.pi
r = int(input())
res = round((r ** 2) * p, 6)  # 유클리드 기하학
res2 = 2 * (r ** 2)  # 택시 기하학 -> 마름모 넓이 구하면 됨
print(f"{res:.6f}")
print(f"{res2:.6f}")
