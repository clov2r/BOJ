T=int(input()) # testcase
birth={} # 생일 정보 저장
for i in range(T):
    X=input() # 문자열 입력 Mickey 1 10 1991
    N, DD, MM, YYYY=X.split() # 이름과 생년월일 분리
    # 문자열로 변환할 때 날짜가 제대로 정렬될 수 있게 한 자리 숫자일 경우 0으로 붙임
    if int(MM)<10:
         MM='0'+MM
    if int(DD)<10:
        DD='0'+DD
    date=int(YYYY+MM+DD) # yyyymmdd형식으로 변환
    birth[date]=N # 날짜를 키로 하고 이름을 값으로 저장
birth=sorted(birth.items()) # 날짜 기준으로 정렬
print(birth[-1][1])
print(birth[0][1])