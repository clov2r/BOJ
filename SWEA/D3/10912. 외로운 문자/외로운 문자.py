T=int(input()) #testcase
for i in range(T): #testcase 만큼 반복
    X=input() #문자열
    X_list=list(X) #문자열을 리스트화
    X2_list=sorted(X_list) #사전 순서대로 출력하기 위함
    X3=set() #짝지어진 문자들을 저장할 집
    for j in range(len(X2_list)): #짝지어진 문자들을 찾음
        if X2_list.count(X2_list[j])%2==0: #짝수개의 문자가 있으면 짝지어짐
            X3.add(X2_list[j])
    res=set(X2_list)-X3
    res2=list(res)
    res3=sorted(res2)
    if len(res3)==0:
        print('#%d Good'%(i+1)) #남는 문자가 없으면 good 출력
    else:
        print('#%d '%(i+1), *res3, sep='') #남는 문자 출력