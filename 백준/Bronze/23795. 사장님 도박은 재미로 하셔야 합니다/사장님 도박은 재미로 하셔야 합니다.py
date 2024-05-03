X=[]
while True:
    i=int(input()) #윤성이가 배팅한 돈 입력
    X.append(i) #배팅한 돈들을 리스트에 넣음
    if i==-1:
        X.pop() #-1 삭제
        break
print(sum(X))