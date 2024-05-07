T=int(input()) #testcase
result=[]
for i in range(T): #testcase 만큼 반복
    A, B, C, D=map(int, input().split())
    res=A/B #앨리스의 승률
    res1=C/D #밥의 승률
    if res==res1:
        result.append('DRAW')
    elif res>res1:
        result.append('ALICE')
    else:
        result.append('BOB')
for j in range(T):
    print('#%d'%(j+1), result[j])
