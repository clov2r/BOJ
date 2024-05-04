T=int(input()) #전체 테스트 케이스의 수
for i in range(T):
    cnt=0
    N=int(input()) #정수의 개수 N
    N_list=list(map(int, input().split())) #각 사람의 소득을 뜻하는 N개의 양의 정수를 받는 리스트
    for j in N_list:
        avg=sum(N_list)/len(N_list) #평균 소득 구하기
        if (j<=avg): #평균 이하의 소득을 가진 사람의 수 구하기
            cnt+=1
    print('#%d'%(i+1), cnt)