def solution(brown, yellow):
    answer = []
    
    for y in range(1, yellow+1):
        if yellow % y == 0:
            x = yellow // y
            if (x+2)*(y+2) - x*y == brown:
                answer = [x+2, y+2]

    answer.sort(reverse=True)
    return answer
