N=int(input())
X=input()
if X.count('B') > X.count('A'):
    print('B')
elif X.count('A') > X.count('B'):
    print('A')
else:
    print('Tie')
