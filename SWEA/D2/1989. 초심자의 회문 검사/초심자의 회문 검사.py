T=int(input()) #테스트 케이스 입력
for i in range(1, T+1): #케이스만큼 반복
    X=input() #문자열 입력
    if(X==X[::-1]): #문자열과 뒤집힌 문자열끼리 비교
        print('#%d'%i, 1) #회문일 때
    else:
        print('#%d'%i, 0) #회문이 아닐 때