import sys
from collections import deque

sys.stdin = open('input.txt')
n, k = map(int, sys.stdin.readline().split())
coin = []
for i in range(n):
    coin.append(int(sys.stdin.readline()))
visited = [False] * (100001)
queue = deque()
for c in coin:
    visited[c] = True
    queue.append(c)

L = 1
while queue:
    length = len(queue)
    for i in range(length):
        value = queue.popleft()
        if value == k:
            print(L)
            exit(0)
        for c in coin:
            if c + value > k:
                continue
            if not visited[c + value]:
                visited[c + value] = True
                queue.append(c + value)

    L += 1

print(-1)
