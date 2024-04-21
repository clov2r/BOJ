X=[]
for i in range(0, 20):
    X.append(i+1) # 1부터 20까지 값을 X 리스트에 쑤셔 넣음
for j in range(10):
    A, B=map(int, input().split()) #구간 범위 입력
    X2=X[A-1:B] #범위만큼 빼옴
    X2=list(X2)
    X[A-1:B]=X2[::-1] #역순
print(*X)
