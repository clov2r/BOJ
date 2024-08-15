T=int(input()) #testcase
for i in range(T):
    cnt=0 # 0의 개수를 받는 변수
    X, Y=map(int, input().split()) # 범위 입력
    for j in range(X, Y+1):
        zero_w=str(j) # 정수를 문자열로 변환
        cnt+=zero_w.count('0') # 문자열 zero_w가 0이 얼마나 있는지 count 메서드를 통해 알 수 있음
    print(cnt)
