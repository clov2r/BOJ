T=int(input()) #testcase
for i in range(T): #testcase 만큼 반복
    N_list=list(map(int, input().split())) #양수 리스트
    N_list.remove(max(N_list)) #최대 수 제거
    N_list.remove(min(N_list)) #최소 수 제거
    res=sum(N_list)/len(N_list) #평균값 출력
    print('#%d'%(i+1), round(res)) #소수점 첫째 자리에서 반올림한 정수 출력