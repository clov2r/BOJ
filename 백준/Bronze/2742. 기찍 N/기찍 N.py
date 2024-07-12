N=int(input())
N_list=[]
for i in range(N):
    N_list.append(i+1)
print(*N_list[::-1], sep='\n')