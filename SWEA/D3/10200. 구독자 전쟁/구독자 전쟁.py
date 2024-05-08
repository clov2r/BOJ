T = int(input())  # testcase 입력 받기
for i in range(T):  # testcase 만큼 반복
    X, Y, Z = map(int, input().split())  # X=설문조사인원수, Y=채널 A를 구독한 사람, Z=채널 B를 구독한 사람
    # A, B 채널 모두 구독하고 있는 사람이 최소 몇 명인지, 최대 몇 명인지 구하기
    if Y + Z > X:  # 만약 A와 B 채널의 구독자 수의 합이 설문조사 인원수를 초과한다면
        print('#%d' % (i + 1), min(Y, Z), Y + Z - X)  # 최소값은 채널 A와 B 중 적은 수의 구독자, 최대값은 초과된 만큼의 차이
    else:  # 설문조사 인원수를 초과하지 않는 경우
        print('#%d' % (i + 1), min(Y, Z), 0)  # 최소값은 채널 A와 B 중 적은 수의 구독자, 최대값은 0