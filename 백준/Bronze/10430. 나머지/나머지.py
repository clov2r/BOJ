A, B, C=input().split()
A=int(A)
B=int(B)
C=int(C)
res=(A+B)%C
res1=((A%C) + (B%C))%C
res2=(A*B)%C
res3=((A%C) * (B%C))%C
print(res)
print(res1)
print(res2)
print(res3)
