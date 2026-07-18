V, E = map(int, input().split())

adj = [[] for _ in range(V)]

for _ in range(E):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

visited = [False] * V

def dfs(node):
    visited[node] = True
    print(node, end=" ")

    for nei in adj[node]:
        if not visited[nei]:
            dfs(nei)

dfs(0)
