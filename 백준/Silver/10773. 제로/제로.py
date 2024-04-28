K=int(input()) #정수 K
K_list=[] #K개의 수를 받을 리스트 생성
for i in range(K):
    k=int(input())
    if k==0:
        K_list.pop() #0일 경우 최근에 쓴 수 삭제
    else:
        K_list.append(k) #0이 아니면 수 더함
print(sum(K_list)) #최종 K_list의 합 구함