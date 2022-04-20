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

q = [[0,start]]

while q :
    now = heapq.heappop(q)
    now_cost = now[0]
    now_location = now[1]

    for i in links[now_location]:
        next_cost = now_cost + i[0]
        next_location = i[1]

        if total_cost[next_location] >= next_cost :
            total_cost[next_location] = next_cost
            
            a = (next_cost,next_location)
            heapq.heappush(q,a)

end_cost = total_cost[end]

print(total_cost[end] * -1)


def back(n,co,backlist):
    for i in links[n]:
        if i[1]+co > end_cost:
           continue 
        elif i[1]+co == end_cost:
            backlist.append(i[1])
            total_list.append(backlist)
            backlist.pop()
            continue
        else:
            backlist.append(i[1])
            back(i[1],i[1]+co,backlist)
            backlist.pop()

tlist =[1]
total_list =[]
back(1,0,tlist)
print(tlist)
# print(total_passed)
# total_passed = set(total_passed)
# sort_passed = []
# for i in total_passed:
#     b = str(i)
#     for j in range(len(b)-1):
#         sort_passed.append(b[j]+b[j+1])

# print(len(set(sort_passed)))