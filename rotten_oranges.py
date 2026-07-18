from collections import deque

m,n=map(int,input().split())
grid=[]
for _ in range(m):
    grid.append(list(map(int,input().split())))

def solution():
    fresh=0
    q=deque()
    for i in range(m):
        for j in range(n):
            if grid[i][j]==2:
                q.append((i,j))
            elif grid[i][j]==1:
                fresh+=1
    if fresh==0:
        return 0
    directions=[(-1,0),(1,0),(0,-1),(0,1)]
    minutes=0
    while q:
        size=len(q)
        for _ in range(size):
            r,c=q.popleft()
            for dr,dc in directions:
                rr=r+dr
                rc=c+dc
                if 0<=rr<m and 0<=rc<n and grid[rr][rc]==1:
                    grid[rr][rc]=2
                    fresh-=1
                    q.append((rr,rc))
        if q:
            minutes+=1
    if fresh==0:
        return minutes
    return -1

print(solution())
