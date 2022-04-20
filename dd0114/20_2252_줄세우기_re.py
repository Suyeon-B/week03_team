from collections import deque
import sys

n, m = map(int,sys.stdin.readline().split())

links = [[] for _ in range(n+1)]
ind = [0]*(n+1)

for i in range(m):
    a, b = map(int,sys.stdin.readline().split())
    links[a].append(b)
    ind[b] += 1

q = deque([])

for i in range(1,n+1):
    if ind[i] ==0:
        q.append(i)

result = []

while q:
    a = deque.popleft(q)
    result.append(a)
    
    for i in links[a]:
        ind[i] -= 1
        if ind[i] == 0:
            q.append(i)


for i in result:
    print(i, end =" ")