T=int(input()) #testcase
for i in range(T): #testcase 만큼 반복
    N, K=map(int, input().split()) #N개의 점수 K개만큼 뽑기
    X=list(map(int, input().split())) #범위가 N인 숫자 리스트 입력
    X2=sorted(X)
    res=X2[-K:]
    print('#%d'%(i+1), sum(res))