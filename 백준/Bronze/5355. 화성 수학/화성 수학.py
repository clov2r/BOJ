T = int(input())

for _ in range(T):
    N = list(map(str, input().split()))
    res = 0
    for i in range(len(N)):
        if i == 0:
            res += float(N[i])
        else:
            if N[i] == "#":
                res -= 7
            elif N[i] == "%":
                res += 5
            elif N[i] == "@":
                res *= 3
                
    print("%0.2f" % res)