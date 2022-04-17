import sys


def search_heavy(start):
    cnt = 0
    for next in heavy[start]:
        cnt +=1
        cnt += search_heavy(next)

    return cnt


def search_light(start):
    cnt = 0
    for next in light[start]:
        cnt += 1
        cnt += search_light(next)

    return cnt


N, M = map(int, sys.stdin.readline().split())
heavy = [[] for _ in range(N+1)]
light = [[] for _ in range(N+1)]

for i in range(M):
    a ,b  = map(int,sys.stdin.readline().split())
    heavy[a].append(b)
    light[b].append(a)

ans = 0
for i in range(1,N+1):
    if search_light(i) >= (N+1)//2 or search_heavy(i) >= (N+1)//2:
        ans +=1


print(ans)

