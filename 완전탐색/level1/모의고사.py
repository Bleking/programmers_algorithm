# 프로그래머스 완전탐색 level 1 모의고사

def solution(answers):
    result = []
    
    std1 = [1, 2, 3, 4, 5]
    std2 = [2, 1, 2, 3, 2, 4, 2, 5]
    std3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    a1, a2, a3 = 0, 0, 0
    for i in range(len(answers)):
        if answers[i] == std1[i % len(std1)]:
            a1 += 1
        if answers[i] == std2[i % len(std2)]:
            a2 += 1
        if answers[i] == std3[i % len(std3)]:
            a3 += 1
    
    if a1 == max(a1, a2, a3):
        result.append(1)
    if a2 == max(a1, a2, a3):
        result.append(2)
    if a3 == max(a1, a2, a3):
        result.append(3)
    
    return result
