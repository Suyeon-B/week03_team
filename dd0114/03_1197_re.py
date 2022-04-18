# prim으로 풀기

import sys
import heapq
input = sys.stdin.readline

V,E = map(int,input().split())
visited = [False]*(V+1)

Elist =[[]for _ in range(V+1)]
heap = [[0,1]]
for _ in range(E):
    s, e, w = map(int, input().split())
    Elist[s].append([w,e])
    Elist[w].append([w,s])

answer = 0 
cnt = 0
while heap:
    if cnt ==V :
        break
    cost,start= heapq.heappop(heap)
    if not visited[start]:
        visited[start] = True
        answer += cost
        cnt +=1
        for i in Elist[start]:
            heapq.heappush(heap, i)
    