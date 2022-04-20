import sys
from collections import deque
m, n, h = map(int,input().split())

box = [[]for _ in range(h)]
result = [[]for _ in range(h)]
q = deque([])

for i in range(h):
    for j in range(n):
        # 박스에 수 받기
        a = list(map(int,sys.stdin.readline().split()))
        box[i].append(a)
        # 익은 토마토면 큐에 넣고 / 방문처리
        for k in range(m):
            if a[k] == 1 :
                box[i][j][k] = -1
                q.append([k,j,i])
        # 최종 검토할 상자만들기
        b = [-1]*m
        result[i].append(b)

dx = [1,0,0,-1,0,0]
dy = [0,1,0,0,-1,0]
dz = [0,0,1,0,0,-1]

year = 0

q2 = deque([])

while q :
    mm, nn, hh = q.popleft()
    for i in range(6):
        new_m = mm+dx[i]
        new_n = nn+dy[i]
        new_h = hh+dz[i]

        if 0<= new_m < m and 0<= new_n <n and 0<= new_h <h:
            if box[new_h][new_n][new_m] == 0:
                box[new_h][new_n][new_m] = -1
                c = [new_m,new_n,new_h]
                q2.append(c)
    
    if q == deque([]) :
        year += 1
        q = q2
        q2 = deque([])

if result == box:
    print(year-1)
else :
    print(-1)
