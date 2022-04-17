import sys
N,M = map(int,sys.stdin.readline().split())
marble = [ [0]*(N) for _ in range(N)]
h = (N+1)//2
for i in range(M):
    a,b = map(int,sys.stdin.readline().split())
    marble[a-1][b-1] = 1

for k in range(N):
    for i in range(N):
        for j in range(N):
            if (marble[i][k] & marble[k][j]) == 1:
                marble[i][j] = 1

ans = 0
for i in range(N):
    h_cnt , l_cnt = 0,0
    for j in range(N):
        if marble[i][j] == 1:
            h_cnt +=1
        if marble[j][i] == 1:
            l_cnt +=1

    if h_cnt >= h or l_cnt >=h:
        ans+=1

print(ans)

