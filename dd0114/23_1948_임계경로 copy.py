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

q = [[0,start,start]]
total_passed = []

while q :
    now = heapq.heappop(q)
    now_cost = now[0]
    now_location = now[1]
    passed = now[2]

    if now_location == end:
        total_passed.append(passed)

    for i in links[now_location]:
        next_cost = now_cost + i[0]
        next_location = i[1]
        new_passed = int(str(passed) + str(next_location))
        
        # 3일때 다음행선지
        if now_location == 3:
            print('here')
            print(next_location)
            print(passed)        
        #  delet

        if total_cost[next_location] >= next_cost :
            total_cost[next_location] = next_cost
            
            a = (next_cost,next_location,new_passed)
            heapq.heappush(q,a)

print(total_cost[end] * -1)
print(total_passed)

print(links)
total_passed = set(total_passed)
sort_passed = []
for i in total_passed:
    b = str(i)
    for j in range(len(b)-1):
        sort_passed.append(b[j]+b[j+1])

print(len(set(sort_passed)))