# 프로그래머스 정렬 K번째수

def solution(array, commands):
    answer = []
    
    for idx in range(len(commands)):
        arr = array[commands[idx][0] - 1 : commands[idx][1]]
        arr = sorted(arr)
        answer.append(arr[commands[idx][2] - 1])
    
    return answer
