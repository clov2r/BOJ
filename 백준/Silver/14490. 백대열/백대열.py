import math
N,M=map(int, input().split(':'))
num=math.gcd(N,M)
print(N//num,':',M//num,sep='')
