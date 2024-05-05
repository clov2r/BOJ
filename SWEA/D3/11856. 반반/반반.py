T=int(input()) #testcase
for i in range(T):
    X=list(input()) # 문자열을 리스트로 변환
    X2=set(X)  # 문자열에서 중복을 제거하여 집합으로 변환
    if len(X2)==2: # 두 개의 서로 다른 문자가 있는 경우
        print('#%d'%(i+1),'Yes')
    else: #아닌 경우
        print('#%d'%(i+1), 'No')
