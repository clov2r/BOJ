import sys
N=int(sys.stdin.readline())
N_list=[]
for i in range(N):
    N_list.append(int(sys.stdin.readline()))
N_list.sort(reverse=True)
print(*N_list, sep='\n')