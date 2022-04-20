import sys
import heapq
from collections import deque

n = int(input())
m = int(input())

ind =[0]*(n+1)
links = [[]for _ in range(n+1)]
total_cost = [0]*(n+1)
total_count = [0]*(n+1)

for i in range(m):
    start, end, cost = map(int,sys.stdin.readline().split())
    links[start].append([cost*-1,end])
    ind[end] += 1

start,end = map(int,sys.stdin.readline().split())

q = [(0,start,0)]

while q :
    now = heapq.heappop(q)
    now_cost = now[0]
    now_location = now[1]
    now_count = now[2]

    for i in links[now_location]:
        next_cost = now_cost + i[0]
        next_location = i[1]
        next_count = now_count+1
        
        if total_cost[next_location] > next_cost :
            total_cost[next_location] = next_cost
            total_count[next_location] = next_count

            a = (next_cost,next_location,next_count)
            heapq.heappush(q,a)
            print(q)

print(total_cost[end] * -1)
print(total_count[end])
