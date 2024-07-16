N, M =map(int, input().split()) # 바구니의 개수 / M번 공
N_list=[i for i in range(1, N+1)]
for x in range(M):
    i, j=map(int, input().split())
    # temp를 사용하지 않는 방법도 존재함
    N_list[i-1], N_list[j-1]=N_list[j-1],N_list[i-1]
    # 두 배열 안에 있는 값을 교환하기 위해 temp 사용
    """temp=N_list[i-1]
    N_list[i-1]=N_list[j-1]
    N_list[j-1]=temp"""
print(*N_list)