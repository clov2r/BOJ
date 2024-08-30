def solution(array, commands):
    answer = []
    # 각 command에 대해 처리
    for command in commands:
        i, j, k = command
        # i부터 j까지 자르고 정렬한 후 k번째 수를 찾음
        sub_array = sorted(array[i-1:j])
        answer.append(sub_array[k-1])
    return answer
