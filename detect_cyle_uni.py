def solution():
    n = 5

    edges = [
        [0,1],
        [0,2],
        [1,2],
        [2,3],
        [3,4]
    ]

    graph = [[] for _ in range(n)]

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = [False] * n

    def dfs(node, parent):
        visited[node] = True

        for nei in graph[node]:
            if not visited[nei]:
                if dfs(nei, node):
                    return True
            elif nei != parent:
                return True

        return False

    has_cycle = False

    for i in range(n):
        if not visited[i]:
            if dfs(i, -1):
                has_cycle = True
                break

    return has_cycle


print(solution())
