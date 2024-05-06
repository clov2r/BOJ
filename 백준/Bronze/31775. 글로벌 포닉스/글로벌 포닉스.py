A=input()
A2=list(A)
B=input()
B2=list(B)
C=input()
C2=list(C)
if A2[0]=='k' and B2[0]=='l' and C2[0]=='p':
    print('GLOBAL')
elif A2[0]=='k' and B2[0]=='p' and C2[0]=='l':
    print('GLOBAL')
elif A2[0]=='l' and B2[0]=='p' and C2[0]=='k':
    print('GLOBAL')
elif A2[0]=='l' and B2[0]=='k' and C2[0]=='p':
    print('GLOBAL')
elif A2[0]=='p' and B2[0]=='k' and C2[0]=='l':
    print('GLOBAL')
elif A2[0]=='p' and B2[0]=='l' and C2[0]=='k':
    print('GLOBAL')
else:
    print('PONIX')