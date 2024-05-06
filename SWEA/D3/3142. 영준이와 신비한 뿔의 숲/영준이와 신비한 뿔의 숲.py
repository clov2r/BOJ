T = int(input())  #testcase
for i in range(T): #testcase 만큼 반복
    N, M=map(int, input().split()) #N=뿔 M=마리
    #연립방정식으로 해결
    X=N-M #트윈혼 마리
    Y=2*M-N #유니콘 마리
    print('#%d'%(i+1), Y, X)