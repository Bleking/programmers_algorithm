# 프로그래머스 그리디 level 1 체육복

def solution(n, lost, reserve):
    lost = sorted(lost)
    reserve = sorted(reserve)
    
    for r in reserve[:]:
        if r in lost:
            reserve.remove(r)
            lost.remove(r)

    for i in range(len(reserve)):
        if reserve[i] - 1 in lost:
            lost.remove(reserve[i] - 1)
        elif reserve[i] + 1 in lost:
            lost.remove(reserve[i] + 1)
    
    answer = n - len(lost)
    
    return answer 
