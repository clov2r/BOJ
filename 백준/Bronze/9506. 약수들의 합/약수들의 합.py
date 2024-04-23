while True: 
    N = int(input())  # 숫자 N 입력받기
    if N == -1:  # 입력이 -1이면 프로그램 종료
        break  # 루프 탈출
    X = []  # N의 약수 리스트
    for i in range(1, N+1):  # 약수 판별
        if N % i == 0:
            X.append(i)
    res = sum(X) - N  # 완전수 판별 (자기 자신을 제외한 모든 약수들의 합이 같으면 완전수)
    if res == N:
        print('%d = ' % N, end='')
        for i in range(len(X)-2):
            print(X[i], end=' + ')
        print(X[-2])
    else:
        print('%d is NOT perfect.' % N)