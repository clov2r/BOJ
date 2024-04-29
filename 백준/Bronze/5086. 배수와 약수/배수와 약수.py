while True: #무한 반복으로 돌리고 두 수가 0일 경우 break
    A, B=map(int, input().split())
    if A==B==0:
        break
    if B%A==0: #A가 B의 약수일 때
        print('factor')
    elif A%B==0: #A가 B의 배수일 때
        print('multiple')
    else: #약수도 아니고 배수도 아닐 때
        print('neither')