import sys
from collections import deque
import copy

n = int(input())

links  = [[] for _ in range(n)]
ind = [0]*n

for i in range(n):
    a = list(map(int,sys.stdin.readline().strip()))
    for j in range(n):
        if a[j] == 1 :
            links[i].append(j)
            ind[j] += 1

parents = [[]for _ in range(n+1)]

q = deque([])
for i in range(n):
    if ind[i] == 0:
        q.append(i)

# 각 숫자 위에 몇개가 있는지 세기
# 스택리스트에 자기 위에 몇개 있는지 표시
# 연결 수 불러올때 연결수 스택에 자신 스택 +1
breaker = 0

while q :
    a = deque.popleft(q)     

    for i in links[a]:
        ind[i] -= 1
        parents[i].append(a)
        parents[i] += parents[a]        

        # ind가 0이면 큐 넣기 
        if ind[i] ==0:
            q.append(i)
            parents[i] = list(set(parents[i]))

# ind가 0이 아니면 순환

if set(ind) != {0}:
    breaker = 1

if breaker != 1:
    result = []
    for i in range(n):
            total = []
            for k in range(n):
                total.append(k)        
            total = set(total)
            maxnum = n

            for j in range(len(result)) :
                if i in parents[j] :
                    maxnum = min(maxnum, result[j])

                elif not j in parents[i] and result[j] < maxnum:
                    total -= set(parents[j])
                    total -= {j}

            total -= set(parents[i])
            total -= {i}
            result.append(n-len(total))

    for i in result:
        print(i,end=' ')

else :
    print(-1)

# 순서표를 만든다.
# 0번 부터 stack+1 넣음. stack+1이 사용중이면 +2 넣으면 패스
# 다음 수로 넘어감