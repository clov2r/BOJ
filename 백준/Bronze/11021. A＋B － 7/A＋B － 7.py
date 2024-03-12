import sys
test=int(input())
for i in range(test):
    a, b=sys.stdin.readline().split()
    a=int(a)
    b=int(b)
    print("Case #%d: " %(i+1), end="")
    print(a+b)
