import sys

def bfs(start):
    distance[start] = 0
    Queue = []
    Queue.append(start)
    while Queue:
        node = Queue.pop(0)
        for nxt in graph[node]:
            if distance[nxt] == -1:
                distance[nxt] = distance[node]+1
                Queue.append(nxt)


N,M,K,X = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
distance = [-1]*(N+1)

for i in range(M):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)

bfs(X)
flag = True
for i in range(1,N+1):
    if distance[i] == K:
        flag = False
        print(i)

if flag == True:
    print(-1)