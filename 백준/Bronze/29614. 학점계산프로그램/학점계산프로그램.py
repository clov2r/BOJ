# 학점 변환 딕셔너리
score = {
    'A+': 4.5, 'A': 4.0,
    'B+': 3.5, 'B': 3.0,
    'C+': 2.5, 'C': 2.0,
    'D+': 1.5, 'D': 1.0,
    'F': 0.0
}

# 사용자로부터 등급 문자열 입력받기
s = input() #A+B+C+D+F

# 등급을 담을 리스트 초기화
res = []

# 문자열을 순회하면서 등급을 분리하여 리스트에 저장
for i in range(len(s)): #A+B+C+D+F를 처음부터 끝까지 순회
    # 현재 문자가 '+'인 경우 건너뛰기
    if s[i] == "+":
        continue

    # 현재 문자와 다음 문자가 '+'이면 두 문자를 하나의 등급으로 저장
    if i + 1 < len(s) and s[i + 1] == "+":
        res.append(s[i:i+2])
    else:
        # 그렇지 않으면 현재 문자만 등급으로 저장
        res.append(s[i])

# 총 학점 계산
total = sum([score[g] for g in res])

# 평균 학점 계산 및 출력
print(total / len(res))
