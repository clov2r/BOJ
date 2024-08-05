all_record={} # 값을 정하는 딕셔너리 생성
for i in range(8):
    rec, T=input().split() # 결과와 팀 입력
    M,SS,SSS=rec.split(':') # 결과를 분, 초, 밀리초로 나눔
    res=float(str(int(M)*60+int(SS)) +'.'+SSS) # 초로 통일함
    all_record[res]=T # res를 키로, 팀을 값으로 딕셔너리에 저장

# 딕셔너리를 오름차순으로 정렬
all_record=sorted(all_record.items())
# 점수 초기화
point=[10,8,6,5,4,3,2,1]
# 팀 점수 초기화
R,B=0,0
for i in range(8):
    if all_record[i][1]=='R': # 정렬된 기록에서 팀을 확인해 팀의 점수 누적
        R+=point[i]
    else:
        B+=point[i]
# 점수 비교 후 이긴 팀 출력
if R>B:
    print('Red')
else:
    print('Blue')
