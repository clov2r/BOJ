def solution(num_list):
    X=[]
    for i in range(len(num_list)):
        if num_list[i]%2==0:
            X.append('ever')
        else:
            X.append('odd')
    A=X.count('ever')
    B=X.count('odd')
    answer = [A, B]
    return answer