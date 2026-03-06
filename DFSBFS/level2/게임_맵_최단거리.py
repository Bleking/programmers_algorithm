# 프로그래머스 DFS/BFS level 2 게임 맵 최단거리

from collections import deque

def solution(maps):
    answer = 0
    
    n, m = len(maps), len(maps[0])
    
    visited = [[False] * m for _ in range(n)]
    
    bfs(maps, 0, 0, n, m, visited)
    
    if visited[n-1][m-1] == False and maps[n-1][m-1] == 1:
        answer = -1
    else:
        answer = maps[n-1][m-1]
    
    return answer

def bfs(maps, r, c, n, m, visited):
    visited[r][c] = True
    
    dr = [-1, 1,  0, 0]
    dc = [ 0, 0, -1, 1]
    
    queue = deque()
    queue.append((r, c))
    
    while queue:
        r, c = queue.popleft()
        
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            
            if 0 <= nr < n and 0 <= nc < m:
                if visited[nr][nc] == False and maps[nr][nc] == 1:
                    visited[nr][nc] = True
                    maps[nr][nc] = maps[r][c] + 1
                    queue.append((nr, nc))
