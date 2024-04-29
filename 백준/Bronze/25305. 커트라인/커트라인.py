N, K=map(int, input().split()) #N명의 학생들이 응시 가장 높은 K만 상을 수여
N_list=list(map(int, input().split())) #N명의 학생들 점수
N_list.sort(reverse=True) #내림차순
print(N_list[K-1])