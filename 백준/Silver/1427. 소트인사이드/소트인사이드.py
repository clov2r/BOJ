T = input() #정렬하려고 하는 T가 주어짐
X = list(T)
X.sort(reverse=True) #내림차순으로 정렬
print(*X, sep='') #공백 없이 출력
