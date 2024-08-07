C, K, P=map(int, input().split()) #와인을 모은 년수, 애착 정도, 구매중독 정도
cnt=0 #수집한 와인 수
for i in range(C+1): 
    cnt+=(K*i)+(P*(i**2)) #해당 년도에 수집한 와인의 수를 계산해 cnt에 더함
print(cnt)