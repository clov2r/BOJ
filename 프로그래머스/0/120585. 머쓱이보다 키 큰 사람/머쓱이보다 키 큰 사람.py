def solution(array, height):
    array2=sorted(array)
    answer = 0
    for i in range(len(array2)):
        if array2[i]>height:
            answer+=1
    return answer