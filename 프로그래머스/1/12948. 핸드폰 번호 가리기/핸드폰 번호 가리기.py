def solution(phone_number):
    if len(phone_number) > 4:
        masked_s = '*' * (len(phone_number) - 4) + phone_number[-4:]
    else:
        masked_s = phone_number  # 문자열의 길이가 4 이하일 경우, 그대로 출력
    return masked_s