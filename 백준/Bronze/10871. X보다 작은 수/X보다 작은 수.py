n, x= input().split()
n=int(n)
x=int(x)
n_list = list(map(int, input().split()))
for num in n_list:
    if(num<x):
        print(num, end=' ')
