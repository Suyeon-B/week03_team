import sys

n,k = map(int,sys.stdin.readline().split())
inf = int(1e9)

coin = []
coin2 = []
q = []
cost = [inf]*(k+1)

for _ in range(n):
    a = int(sys.stdin.readline())
    if a <= k :
        coin.append(a)
        coin2.append(a)
        q.append(a)
        cost[a] = 1

q2 = []
answer = -1
save_cost = inf

q.sort()
coin.sort()
coin2.sort()

while q :
    c = q.pop(0) 

    for i in coin2 :
        next_coin = c+i 
        new_cost = cost[c]+cost[i] 
        
        print

        if next_coin == k :
            answer = 0
            save_cost = new_cost 

        if save_cost < new_cost:
            break

        if next_coin > k :
            continue

        else:
            if cost[next_coin] > new_cost:
                cost[next_coin] = new_cost
                q2.append(next_coin)
                coin.append(next_coin)

    if q == []:
        q = q2
        q2 = []
        coin2 = coin[:]
        if  answer == 0 :
            print(cost[k])
        
            exit(0)

if answer == -1:
    print(answer)