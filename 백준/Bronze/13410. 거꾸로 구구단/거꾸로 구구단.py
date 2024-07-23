N, K=map(int, input().split())
rev_res=[]
for i in range(1, K+1):
    x=str(N*i)
    rev_res.append(int(x[::-1]))  # 역순 문자열을 정수로 변환하여 리스트에 추가
print(max(rev_res))

