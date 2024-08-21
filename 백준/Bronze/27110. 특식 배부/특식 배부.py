N=int(input()) # 각 종류의 치킨 마릿수
lst=list(map(int, input().split())) # 후라이드 A, 간장치킨 B, 양념치킨 C
tot=0 # 최대 선호 치킨
for i in range(3): # 각 치킨 종류에 대해 반복문 실행
    if N>=lst[i]: # 만약 치킨의 선호 인원이 치킨 마릿수보다 작거나 같다면, 모두 받을 수 있음
        tot+=lst[i]
    elif N<lst[i]: # 만약 치킨의 선호 인원이 주문한 치킨 마릿수보다 많으면 N명만 받을 수 있음
        tot+=N
print(tot)