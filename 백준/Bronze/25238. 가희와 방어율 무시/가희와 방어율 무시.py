A, B=map(int, input().split())
res=A*(B/100)
if A-res<100:
    print(1)
else:
    print(0)