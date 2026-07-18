 n = int(input())
is_connected = []

for _ in range(n):
    row = list(map(int, input().split()))
    is_connected.append(row)

def solution():
    visited = set()
    provinces = 0

    def dfs(city):
        visited.add(city)

        for nei in range(n):
            if is_connected[city][nei] == 1 and nei not in visited:
                dfs(nei)

    for city in range(n):
        if city not in visited:
            provinces += 1
            dfs(city)

    return provinces

print(solution())
