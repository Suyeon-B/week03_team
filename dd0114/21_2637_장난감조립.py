import sys
from collections import deque

n = int(input())
m = int(input())

ind = [0]* (n+1)
blue_print = [([0]*n) for _ in range(n+1)]
total = [([0]*n) for _ in range(n+1)]
parent_child = [[]for _ in range(n+1)]

for _ in range(m):
    goal, parts, num = map(int,sys.stdin.readline().split())
    ind[goal] +=1
    blue_print[goal][parts] = num
    parent_child[parts].append(goal)

q = deque([])


for i in range(1,n):
    if ind[i] ==0 :
        q.append(i)
        total[i][i] = 1

while q :
    a = deque.popleft(q)
    
    for i in parent_child[a]:
        ind[i] -= 1
        multi= blue_print[i][a]
        
        for j in range(n):
            total[i][j] += (total[a][j])*multi

        if ind[i] ==0:
            q.append(i)

for i in range(n):
    if total[n][i] :
        print(i,total[n][i])

        # 현재 부품 += 필요한 전체 부품(토탈) * 필요 부품 갯수(설계도)
        # 부품 개수를 이관 a의 개수가 필요한만큼
        # 설계도 개수 만큼 토탈에서 복사해서 넣는다