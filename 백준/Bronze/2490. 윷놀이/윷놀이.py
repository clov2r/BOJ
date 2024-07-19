N_list=[]
for i in range(3):
    N_list=list(map(int, input().split()))
    if N_list.count(1)==3:
        print('A')
    elif N_list.count(1)==2:
        print('B')
    elif N_list.count(1)==1:
        print('C')
    elif N_list.count(1)==4:
        print('E')
    else:
        print('D')