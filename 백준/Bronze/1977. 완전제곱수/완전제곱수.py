import math

M=int(input())
N=int(input())
X=[] #제곱수 저장
res=[] #제곱수를 다시 제곱해 저장할 리스트
for i in range(M, N+1):
    sqrt_value = math.sqrt(i) #i의 제곱근 계산
    if sqrt_value == int(sqrt_value):  # 제곱근이 정수인지 확인
        X.append(int(sqrt_value))  # 정수 제곱근을 리스트에 추가

if len(X)==0: #정수 제곱근이 없을 때
    print(-1)
else:
    for i in range(len(X)):
        res.append(X[i]**2) # 저장된 정수 제곱근을 다시 제곱해 res 리스트에 추가
    print(sum(res)) # 모든 제곱수의 합 출력
    print(min(res)) # 최솟값 출력