from datetime import datetime

T=int(input())  # 사용자로부터 입력받는 테스트 케이스의 수
for i in range(1, T+1):
    A, B, C, D=map(int, input().split())  # 각각의 입력을 정수형으로 변환하여 A, B, C, D에 할당
    X = datetime(2023, A, B)  # A와 B를 이용하여 2024년의 날짜 객체 생성
    Y = datetime(2023, C, D)  # C와 D를 이용하여 2024년의 또 다른 날짜 객체 생성
    Z = X - Y  # 두 날짜 간의 차이 계산
    print('#%d'%i, abs(Z.days)+1)  # 차이의 절댓값을 날짜 수로 출력하고, 문제의 요구에 따라 1을 더함
