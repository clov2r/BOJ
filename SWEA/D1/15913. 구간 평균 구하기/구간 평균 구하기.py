T = int(input())  # testcase
for i in range(T):  # testcase 만큼 반복
    N_list = list(map(int, input().split()))  # 10개의 정수 리스트
    M, K = map(int, input().split())
    X_list = N_list[M-1:K]  # 순서를 1부터 시작하므로 인덱스에 -1
    res = sum(X_list) // len(X_list)  # 평균을 소수점 이하는 버리고 정수로 출력
    print('#%d' % (i+1), res)