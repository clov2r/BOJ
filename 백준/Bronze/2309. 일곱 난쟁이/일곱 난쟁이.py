X=[] #9명의 난쟁이들의 키를 입력받는 리스트
for i in range(9):
    X.append(int(input()))    
X.sort() #난쟁이들의 키를 오름차순으로 정렬    
for a in range(len(X)): # 일곱 난쟁이의 키를 찾는 반복문
    for b in range(a+1, len(X)):
        for c in range(b+1, len(X)):
            for d in range(c+1, len(X)):
                for e in range(d+1, len(X)):
                    for f in range(e+1, len(X)):
                        for g in range(f+1, len(X)):
                            if X[a]+X[b]+X[c]+X[d]+X[e]+X[f]+X[g]==100: # 일곱 난쟁이의 키의 합이 100이 되는 경우를 찾음
                                print(X[a], X[b], X[c], X[d], X[e], X[f], X[g], sep='\n')
                                exit()
