N=input()
mid=len(N)//2
numbers=list(map(int, N)) #문자열을 정수 리스트로 변환
lt=numbers[:mid] #반으로 나눠서 왼쪽
rt=numbers[mid:] #반으로 나눠서 오른쪽
# 합이 같으면 LUCKY 출력, 아니면 READY 출력
if sum(lt)==sum(rt):
    print("LUCKY")
else:
    print("READY")
