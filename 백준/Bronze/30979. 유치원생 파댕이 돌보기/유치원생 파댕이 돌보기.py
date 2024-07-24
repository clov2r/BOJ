T=int(input()) # 시간
N=int(input()) # 사탕 개수
N_list=list(map(int, input().split())) # 각 사탕의 맛을 나타내는 List 생성 총 N개가 생성됨
res=sum(N_list)
if res >= T:
    print('Padaeng_i Happy')
else:
    print('Padaeng_i Cry')
