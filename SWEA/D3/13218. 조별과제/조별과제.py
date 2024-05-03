T = int(input())  # 테스트케이스 수를 입력받음
for _ in range(T):  # 테스트케이스 수만큼 반복
    N = int(input())  # 학생의 수를 입력받음
    quotient = N // 3  # 학생 수를 3으로 나눈 몫을 구함
    print('#%d' % (_ + 1), quotient)  # 몫을 출력