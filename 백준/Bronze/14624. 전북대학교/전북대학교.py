N=int(input())
if N%2==0:
    print('I LOVE CBNU')
else:
    print('*'*N)
    print(" "*(N//2)+"*")
    for i in range(N//2):
        print(" "*(N//2 - i - 1)+"*"+" "*(1+i*2)+"*")
