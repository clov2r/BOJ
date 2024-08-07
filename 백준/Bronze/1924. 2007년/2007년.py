# Day 변수를 초기화합니다. 이 변수는 기준 날짜로부터의 총 일수를 저장합니다.
Day = 0

# 각 달의 일수를 저장한 리스트입니다. 2007년은 윤년이 아니므로 2월은 28일입니다.
arrList = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# 요일을 저장한 리스트입니다. 인덱스 0이 "SUN"이며, 6이 "SAT"입니다.
weekList = ["SUN", "MON","TUE", "WED", "THU", "FRI", "SAT"]

# 사용자로부터 입력을 받습니다. 입력된 값을 x와 y에 각각 저장합니다.
x, y = map(int,input().split())

# 입력된 달 전까지의 총 일수를 계산합니다.
for i in range(x-1):
    Day = Day + arrList[i]

# 현재 달의 일수를 더합니다.
# +1을 하지 않는 이유는 1월 1일부터의 차이를 계산하기 위해서입니다.
Day = (Day + y) % 7

# 총 일수를 7로 나눈 나머지를 인덱스로 사용하여 요일을 출력합니다.
print(weekList[Day])
