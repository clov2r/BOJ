N=int(input())
week=7*24*3600
res=1
for i in range(1, N+1):
    res *=i
print(res//week)

