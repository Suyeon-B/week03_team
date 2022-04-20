import sys
import heapq
inf = int(1e9)

n = int(input())
m = int(input())

links =[[] for _ in range(n+1)]

for i in range(m):
    a,b,c = map(int, sys.stdin.readline().split())
    links[a].append([c,b])

start,end = map(int,input().split())

distance = [inf]*(n+1)

def dijkstra(n):
    global dist
    q = []
    # 시작노드 (경로,도착점) 자신으로 가는 경로 (0,자신)
    heapq.heappush(q,(0,n))
    distance[n] = 0
    while q:
        dist,now = heapq.heappop(q)

        if distance[now] < dist :
            continue

        for i in links[now]:
            cost = dist + i[0]

            if cost < distance[i[1]]:
                distance[i[1]] = cost
                heapq.heappush(q,(cost,i[1]))

dijkstra(start)
print (distance[end])
