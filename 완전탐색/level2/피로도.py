# 프로그래머스 완전탐색 level 2 피로도

from itertools import permutations

def solution(k, dungeons):
    dungeon_perm = permutations(dungeons, len(dungeons))

    result = []
    for d in dungeon_perm:
        answer = 0
        life = k
        
        for i in range(len(d)):
            if life >= d[i][0]:
                life -= d[i][1]
                answer += 1
        
        result.append(answer)
    
    return max(result)
