import sys
import copy

n = int(input())

maze = []

for i in range(n):
    a = list(map(int,sys.stdin.readline().strip()))
    maze.append(a)

visited = [([0]*n) for _ in range(n)]
sparevist = copy.deepcopy(visited)

q = [(0,0)]
visited[0][0] = 1

dx = [1,0,-1,0]
dy = [0,1,0,-1]

spare =[]
count = 0

while q != [] :
    x,y = q.pop(0)

    # for i in visited:
    #     print(i)
    # print()
    if x==n and y ==n:
        print(count)
        exit()

    for i in range(4):
        nx,ny = x+dx[i], x+dy[i]
        
        if n > nx >=0 and n > ny >= 0 :
            if visited[ny][nx] == 0:
                
                if maze[ny][nx] == 1 :
                    q.append((nx,ny))
                    visited[ny][nx] = 1

                elif maze[ny][nx] == 0 and sparevist[ny][nx]==0  :                 
                    spare.append((nx,ny))
                    sparevist[ny][nx] = 1

    print(q)
    if q == []:
        count += 1
        q += spare