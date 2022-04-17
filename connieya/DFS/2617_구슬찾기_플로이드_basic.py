import sys
N,M = map(int,sys.stdin.readline().split())
marble = [ [0]*(N+1) for _ in range(N+1)]
h = (N+1)//2
for i in range(M):
    a,b = map(int,sys.stdin.readline().split())
    marble[a][b] = 1

for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            if marble[i][k] == 1 and marble[k][j] == 1:
                marble[i][j] = 1

ans = 0
for i in range(1,N+1):
    h_cnt , l_cnt = 0,0
    for j in range(1,N+1):
        if marble[i][j] == 1:
            h_cnt +=1
        if marble[j][i] == 1:
            l_cnt +=1

    if h_cnt >= h or l_cnt >=h:
        ans+=1

print(ans)