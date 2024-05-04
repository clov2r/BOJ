T=int(input()) #전체 테스트 케이스의 수
remove_list=['a','i','o','u','e'] #모음 리스트
for i in range(T):
    X=input() #문자열 입력
    X_list = list(X) #문자열 요소를 리스트로 쪼갬
    res=[i for i in X_list if i not in remove_list] #모음을 제거한 X_list
    print('#%d '%(i+1), *res, sep='')
