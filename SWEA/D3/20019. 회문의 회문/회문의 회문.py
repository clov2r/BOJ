T = int(input())  #testcase
for i in range(T): #testcase 만큼 반복
    N = input()  #문자열 입력
    N2 = list(N)  #문자열을 한 글자씩 리스트로 변환
    mid = len(N2) // 2  #중간값을 계산하여 회문 여부를 판단할 기준으로 사용
    lt = N2[:mid]  #중간값을 기준으로 왼쪽 부분
    rt = N2[mid + 1:]  #중간값을 기준으로 오른쪽 부분
    if lt == rt:  # 왼 오가 같으면 회문의 회문
        print('#%d' % (i + 1), 'YES')
    else:  #왼 오가 같지 않으면
        print('#%d' % (i + 1), 'NO')  #회문의 회문이 아님