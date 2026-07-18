def dfs(node):
    visited[node] = True
    pathVisited[node] = True

    for nei in graph[node]:

        if not visited[nei]:
            if dfs(nei):
                return True

        elif pathVisited[nei]:
            return True

    pathVisited[node] = False
    return False
