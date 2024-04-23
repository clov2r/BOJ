N, K=map(int, input().split()) # N과 K를 입력
N_list=list(map(int, input().split())) #N의 길이만큼 리스트 생ㅇ성
N_list2=sorted(N_list) #오름차순 정렬
print(N_list2[K-1]) #앞에서 K번째 있는 수 구함 