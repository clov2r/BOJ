import math
N=math.factorial(int(input())) #N!구함
N_list=list(str(N)) #N! 값을 하나하나씩 쪼개서 리스트화시킴
cnt=0
for i in N_list[::-1]: #뒤에서부터 반복함
    if i == '0':
        cnt+=1
    else:
        break
print(cnt)