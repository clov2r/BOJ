N_list=[] #첫번째 줄에서 열번째 줄까지 입력 값을 받는 리스트
X_list=[] #N_list에 있는 요소를 42로 나눈 나머지 값을 받는 리스트
for i in range(10):
    N_list.append(int(input()))
for j in range(10):
    X_list.append(N_list[j]%42)
print(len(set(X_list))) #중복 제거하기 위해 set 집합 메서드 사용