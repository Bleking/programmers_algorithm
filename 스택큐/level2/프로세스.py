from collections import deque

def solution(priorities, location):
    answer = 0
    queue = deque()
    for i in range(len(priorities)):
        queue.append((i, priorities[i]))  # deque([(0, 2), (1, 1), (2, 3), (3, 2)])
    
    while queue:
        maximum = max(queue, key=lambda x: x[1])
        now = queue.popleft()
        
        if now[1] < maximum[1]:
            queue.append(now)
        elif now[1] >= maximum[1]:
            answer += 1
            if now[0] == location:
                break
    
    return answer
