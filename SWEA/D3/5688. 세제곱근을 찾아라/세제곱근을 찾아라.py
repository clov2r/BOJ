T=int(input()) #testcase
for i in range(T): #testcase 만큼 반복
    N=int(input()) #양의 정수 입력
    X=1 #초기 X 값 설정
    found = False #X^3==N인지 여부를 저장할 변수
    while X**3<=N: #X^3이 N 이하인 동안 반복
        if X**3==N: # X^3이 N과 같으면 X 출력 후 found를 True로 변경하고 반복 종료
            print('#%d'%(i+1), X)
            found=True
            break
        X+=1 #X를 1 증가시킴        
    if not found: #X^3이 N이 아닌 경우 -1 출력
        print('#%d'%(i+1), -1)
