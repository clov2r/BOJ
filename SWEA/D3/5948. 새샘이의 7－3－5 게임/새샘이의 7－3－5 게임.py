T=int(input()) #testcase
for i in range(T): #testcase 만큼 반복
    com=set()
    X=list(map(int, input().split())) #범위가 7인 숫자 리스트 입력
    for j in range(0, len(X)):
        for t in range(j+1, len(X)):
            for x in range(t+1, len(X)):
                res=X[j]+X[t]+X[x] #리스트 중에서 3개의 값을 뽑아 더함
                com.add(res) #중복값을 제외한 값들만 넣음
    com2=list(com) #다시 리스트화
    com3=sorted(com2) #정렬
    print('#%d'%(i+1), com3[-5]) #5번째로 큰 수 출력
