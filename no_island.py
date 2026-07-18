m,n=map(int,input().split())
grid=[]
for _ in range(m):
    row = list(map(int, input().split()))
    grid.append(row)
  
def solution():
    island=0
    visited=set()

    def dfs(row,col):
        if row<0 or row>=m or col<0 or col>=n:
            return
        if grid[row][col]==0:
            return
        if (row,col) in visited:
            return
        visited.add((row,col))
        dfs(row+1,col)
        dfs(row-1,col)
        dfs(row,col+1)
        dfs(row,col-1)
    for i in range(m):
        for j in range(n):
            if grid[i][j]==1 and (i,j) not in visited:
                island+=1
                dfs(i,j)
    return island
        
print(solution())
            
