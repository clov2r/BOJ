x=[] #x좌표
y=[] #y좌표
res=[] #찾아야 할 좌표
for i in range(3):
    a, b=map(int, input().split()) #좌표 입력
    x.append(a)
    y.append(b)
# x와 y 좌표 중에서 하나만 나타나는 값을 찾기
for i in range(3):
    if x.count(x[i])==1:
        res.append(x[i])
for i in range(3):
    if y.count(y[i])==1:
        res.append(y[i])
print(*res)
