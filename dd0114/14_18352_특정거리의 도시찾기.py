import sys

n, m, goal, start = map(int, sys.stdin.readline().split())

links = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int,sys.stdin.readline().split())
    links[a].append(b)

visited = [0]*(n+1)
q = [start]
length = [0]*(n+1)
visited[start] = 1

while q:
    a= q.pop(0)

    if length[a] == goal :
        break

    for i in links[a]:
        if visited[i] ==0 :
            q.append(i)
            visited[i] = 1
            length[i] = length[a]+1

count = 0
for i in range(len(length)) :
    if length[i] == goal :
        print(i)
        count += 1
    
if count == 0:
    print(-1)