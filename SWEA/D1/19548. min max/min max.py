T=int(input()) #testcase
for i in range(T): #testcase 만큼 반복
    N=int(input()) #양수의 개수 N
    N_list=list(map(int, input().split())) #N개의 양수 리스트
    print('#%d'%(i+1), max(N_list)-min(N_list)) #가장 큰 수와 가장 작은 수 차이 출력