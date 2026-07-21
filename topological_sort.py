from collections import deque

n, m = map(int, input().split())

graph = [[] for _ in range(n)]
indegree = [0] * n

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    indegree[v] += 1

q = deque()

for i in range(n):
    if indegree[i] == 0:
        q.append(i)

ans = []

while q:
    node = q.popleft()
    ans.append(node)

    for nei in graph[node]:
        indegree[nei] -= 1
        if indegree[nei] == 0:
            q.append(nei)

if len(ans) == n:
    print(*ans)
else:
    print("Cycle detected")
