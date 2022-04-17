import sys

sys.setrecursionlimit(10 ** 4)

def meltIceberg():
    for i in range(N):
        for j in range(M):
            if iceberg[i][j] <= 0:
                for idx in range(4):
                    nx = dx[idx]+i
                    ny = dy[idx]+j
                    if nx < 0 or nx >= N or ny < 0 or ny >= M:
                        continue
                    if iceberg[nx][ny] > 0 :
                        sea[nx][ny] += 1


    for i in range(N):
        for j in range(M):
            iceberg[i][j] -= sea[i][j]


def dfs(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if iceberg[nx][ny] > 0 and sea[nx][ny] == 0:
            sea[nx][ny] = 1
            dfs(nx, ny)


def countIceBerg():
    global sea
    sea = [[0] * M for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(M):
            if iceberg[i][j] > 0 and sea[i][j] == 0:
                sea[i][j] = 1
                dfs(i, j)
                cnt += 1

    sea = [[0] * M for _ in range(N)]
    return cnt


N, M = map(int, sys.stdin.readline().split())
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
iceberg = []
T = 1
sea = [[0] * M for _ in range(N)]
for i in range(N):
    iceberg.append(list(map(int, sys.stdin.readline().split())))

while True:
    meltIceberg()
    cnt = countIceBerg()
    if cnt > 1 or cnt == 0:
        if cnt == 0:
            T = 0
        break
    T += 1

print(T)
