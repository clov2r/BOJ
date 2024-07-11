N=input() #길이가 N인 단어 주어짐
N_len=len(N)
for i in range(0, len(N), 10): #반복문을 10씩 증가시킴
    print(N[i:i+10]) #문자열을 10단위로 끊어줌