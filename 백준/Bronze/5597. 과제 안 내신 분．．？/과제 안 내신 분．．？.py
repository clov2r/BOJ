X=[i for i in range(1, 31)] # 1번부터 30번까지 있는 정석 출석부
T=[] # 과제 제출한 출석부
for i in range(28): #제출한 사람 입력 받기
    T.append(int(input()))
res=list(set(X)-set(T)) #set을 사용해서 중복된 요소를 제거한 후 다시 리스트로 변환
res2=sorted(res) 
print(res2[0]) #출석번호 중 가장 작은 거 -> 귀찮아서 정렬 시킴
print(res2[1]) #그 다음 거 출력