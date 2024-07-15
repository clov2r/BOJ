N=int(input()) # N개의 정수
N_list=list(map(int, input().split())) # 최솟값 최댓값을 구하는 배열
print(min(N_list), max(N_list))