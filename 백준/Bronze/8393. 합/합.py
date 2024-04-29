n=int(input()) #1부터 n까지의 합을 구하기 위해 n 입력 받음
res=0 # 결과값
for i in range(1, n+1): #1부터 n까지 반복
    res+=i #+= 연산자로 결과값 계속 수정?
print(res)