from collections import deque

V, E = map(int, input().split())

adj = [[] for _ in range(V)]

for _ in range(E):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

visited = [False] * V

def bfs(start):
    q = deque([start])
    visited[start] = True

    while q:
        node = q.popleft()
        print(node, end=" ")

        for nei in adj[node]:
            if not visited[nei]:
                visited[nei] = True
                q.append(nei)

bfs(0)
