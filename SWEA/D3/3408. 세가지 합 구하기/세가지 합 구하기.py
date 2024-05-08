T=int(input()) #testcase
for i in range(T): #testcase 만큼 반복
    N=int(input())
    S1=((N+1)*N) // 2
    # 양의 정수 중 홀수인 것들 중에서 작은 순서대로 N개의 합
    S2=N ** 2
    # 양의 정수 중 짝수인 것들 중에서 작은 순서대로 N개의 합
    S3=(N+1)*N
    print('#%d'%(i+1), S1, S2, S3)