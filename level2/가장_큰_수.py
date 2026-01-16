# 프로그래머스 정렬 level 2 가장 큰 수 

def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers))
    
    num_sorted = sorted(numbers, key=lambda x: x*3, reverse=True)
    answer += ''.join(num_sorted)
    
    return str(int(answer))
