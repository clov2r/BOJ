A, B=map(int, input().split()) #A, B 길이 입력
A_list=list(map(int, input().split())) #A길이인 리스트 입력
B_list=list(map(int, input().split())) #B길이인 리스트 입력
C_list=A_list+B_list # 배열 합치기
C_list2=sorted(C_list) #배열을 합친 후 정렬
print(*C_list2) #결과 출력