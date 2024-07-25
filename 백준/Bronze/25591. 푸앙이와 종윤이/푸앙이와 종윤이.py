A, B=map(int, input().split()) #양의 정수 2개 입력
a=100-A
b=100-B
c=100-(a+b)
d=a*b
q= d//100
r= d%100
print(a, b, c, d, q, r)
if (d>=100):
    print(c+q, r)
else:
    print(c, d)