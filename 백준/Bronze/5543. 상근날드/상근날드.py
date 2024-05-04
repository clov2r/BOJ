A=int(input()) #상덕버거
B=int(input()) #중덕버거
C=int(input()) #하덕버거
D=int(input()) #콜라
E=int(input()) #사이다
X=[A+D, A+E, B+D, B+E, C+D, C+E] #세트들의 가격
print(min(X)-50) #제일 저렴한 세트
