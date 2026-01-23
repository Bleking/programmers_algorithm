# 프로그래머스 그리디 level 2 구명보트 

from collections import deque

def solution(people, limit):
    answer = 0
    people = deque(sorted(people))
    
    while len(people) > 1:
        if people[0] + people[-1] <= limit:  # 양 끝 사람 무게 합이 최대 무게를 만족하면
            answer += 1  # 보트 추가
            people.pop()  # 둘 다 제거
            people.popleft()
        else:  # 최대 무게를 넘으면
            answer += 1  # 보트 추가
            people.pop()  # 무거운 사람 먼저
    
    if people:  # 다 제거하고 사람이 남으면
        answer += 1  # 보트 추가
    
    return answer
