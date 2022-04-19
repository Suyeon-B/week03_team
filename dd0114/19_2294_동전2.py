import sys
import heapq

n,k = map(int,sys.stdin.readline().split())
inf = int(1e9)

coin = []

for _ in range(n):
    coin.append(int(input()))

cost = [inf]*(k+1)

for i in coin:
    cost[i] = 1

q = coin

while q :
    c = q.pop(0) 

    for i in coin :
        next_coin = c+i 
        new_cost = cost[c]+cost[i] 
        if c+i == k:
            print(new_cost)
        elif c+i > k :
            continue
        else:
            if cost[next_coin] > new_cost:
                cost[next_coin] = new_cost
                q.append(next_coin)
                coin.append(next_coin)

        