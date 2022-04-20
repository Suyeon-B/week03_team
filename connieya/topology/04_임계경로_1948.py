import sys
from collections import deque

sys.stdin = open('input.txt')

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

road = [[] for _ in range(n + 1)]
road_r = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)
road_time = [0] * (n + 1)
visited = [False] * (n + 1)


def topology(start):
    queue = deque()
    queue.append(start)

    while queue:
        now = queue.popleft()
        for next, time in road[now]:
            indegree[next] -= 1
            road_time[next] = max(road_time[next], time + road_time[now])
            if indegree[next] == 0:
                queue.append(next);

    return road_time[end]


def topology_r(end):
    queue = deque()
    queue.append(end)
    count = 0
    while queue:
        now = queue.popleft()
        for next, time in road_r[now]:
            if road_time[now] - time == road_time[next]:
                count += 1
                if not visited[next]:
                    visited[next] = True
                    queue.append(next)
    return count


for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    road[a].append((b, c))
    road_r[b].append((a, c))
    indegree[b] += 1

start, end = map(int, sys.stdin.readline().split())

print(topology(start))
print(topology_r(end))
