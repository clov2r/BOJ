X=input()
for i in range(len(X)):
    #X[i].isupper() 대문자면 True로 변환함
    if(X[i].isupper()==True):
        print(X[i],end='')  #한줄로 출력해야해서