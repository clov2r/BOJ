X, Y, Z=map(int, input().split()) # 대각선, 세로, 가로 비율
res=X/(Y**2+Z**2)**(1/2) # 대각선 길이를 비율의 제곱합의 제곱근으로 나눔
print(int(res*Y), int(res*Z)) # 구한 비율에 세로 가로를 곱해서 실제 길이를 계산
