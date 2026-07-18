m, n = map(int, input().split())

grid = []
for _ in range(m):
    row = list(map(int, input().split()))
    grid.append(row)

sr = int(input())
sc = int(input())
color = int(input())

def solution():
    original_color = grid[sr][sc]

    # Edge case: if the new color is the same as the original
    if original_color == color:
        return grid

    visited = set()

    def dfs(row, col):
        # Out of bounds
        if row < 0 or row >= m or col < 0 or col >= n:
            return

        # Different color
        if grid[row][col] != original_color:
            return

        # Already visited
        if (row, col) in visited:
            return

        visited.add((row, col))
        grid[row][col] = color

        dfs(row + 1, col)
        dfs(row - 1, col)
        dfs(row, col + 1)
        dfs(row, col - 1)

    dfs(sr, sc)
    return grid

ans = solution()

for row in ans:
    print(*row)
