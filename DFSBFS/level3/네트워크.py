# 프로그래머스 DFS/BFS level 3 네트워크

def solution(n, computers):
    answer = 0
    graph = [[]]
    for i in range(n):
        temp = []
        for j in range(n):
            if j != i and computers[i][j] == 1:
                temp.append(j+1)
        graph.append(temp)
    
    visited = [False] * (n+1)
    
    for i in range(1, n + 1):
        if visited[i] == False:
            dfs(graph, i, visited)
            answer += 1
            
    return answer

def dfs(graph, node, visited):
    visited[node] = True
    
    for next in graph[node]:
        if visited[next] == False:
            dfs(graph, next, visited)
