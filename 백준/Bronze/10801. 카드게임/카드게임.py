X = list(map(int, input().split()))  # X가 제시한 숫자
Y = list(map(int, input().split()))  # Y가 제시한 숫자
res = [x - y for x, y in zip(X, Y)]  # 각 숫자 간의 차이를 계산하여 리스트로 저장

minus = 0
plus = 0
zero = 0

for i in res:
    if i < 0:
        minus += 1
    elif i == 0:
        zero += 1
    else:
        plus += 1

if plus > minus: #X리스트가 이긴 경우
    print('A')
elif plus < minus: #Y리스트가 이긴 경우
    print('B')
else: #비길 때
    print('D')
