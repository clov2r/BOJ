from collections import Counter

def solution(participant, completion):
    # 각 배열의 요소 개수를 세어줍니다.
    participant_count = Counter(participant)
    completion_count = Counter(completion)

    # completion에 없는 참가자를 찾아서 반환합니다.
    for person in participant_count:
        if participant_count[person] != completion_count[person]:  
            return person