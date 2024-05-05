T=int(input()) #testcase
for i in range(T):
    X=input() #내일 이후의 가장 빠른 일요일 세기
    if X=='SUN':
        print('#%d'%(i+1), 7)
    elif X=='MON':
        print('#%d'%(i+1), 6)
    elif X=='TUE':
        print('#%d'%(i+1), 5)
    elif X=='WED':
        print('#%d'%(i+1), 4)
    elif X=='THU':
        print('#%d'%(i+1), 3)
    elif X=='FRI':
        print('#%d'%(i+1), 2)
    elif X=='SAT':
        print('#%d'%(i+1), 1)
