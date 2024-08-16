N=int(input())
cnt=0 # 순서쌍의 개수
for i in range(1, int(N**0.5) + 1): # N번을 돌면 시간 초과 발생 -> 루트 N까지 반복
    if N%i==0: #i가 N의 약수인 경우 순서쌍 +1
        cnt+=1
        if i!=N//i: #i와 N//i가 다른 경우, 중복을 피하기 위함
            cnt+=1
print(cnt)
