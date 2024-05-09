T=int(input()) #testcase
for i in range(T): #testcase 만큼 반복
    N_list=list(map(int, input().split())) #5개의 양수 리스트
    max_num=max(N_list) #최고점
    min_num=min(N_list) #최저점
    N_list.remove(max_num)
    N_list.remove(min_num)
    res=max(N_list)-min(N_list) #최고점 - 최저점의 차이가 4 이상 나면 KIN 출력
    if res>=4:
        print('KIN')
    else:
        print(sum(N_list))
