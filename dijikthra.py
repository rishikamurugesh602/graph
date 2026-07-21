import heapq

n, m = map(int, input().split())

graph = [[] for _ in range(n)]

for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

source = int(input())

dist = [float('inf')] * n
dist[source] = 0

heap = []
heapq.heappush(heap, (0, source))

while heap:
    d, node = heapq.heappop(heap)

    if d > dist[node]:
        continue

    for nei, wt in graph[node]:
        if d + wt < dist[nei]:
            dist[nei] = d + wt
            heapq.heappush(heap, (dist[nei], nei))

print(dist)
