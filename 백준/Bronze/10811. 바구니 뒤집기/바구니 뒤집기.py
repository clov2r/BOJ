N, M=map(int, input().split()) # 바구니 개수 N과 반복횟수 M
N_list=[i for i in range(1, N+1)] # 리스트 선언 후 값을 1~N으로 설정
for x in range(M): # M번 반복 i번째와 j번째 있는 요소들만 거꾸로 역순
    i, j=map(int, input().split())
    N_list[i-1:j]=N_list[i-1:j][::-1]
print(*N_list) # 모든 순서를 바꾼 후 출력