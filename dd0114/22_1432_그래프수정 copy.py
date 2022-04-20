import sys
from collections import deque

n = int(input())

links  = [[] for _ in range(n)]
ind = [0]*n

for i in range(n):
    a = list(map(int,sys.stdin.readline().strip()))
    for j in range(n):
        if a[j] == 1 :
            links[i].append(j)
            ind[j] += 1

q = deque([])

for i in range(n):
    if ind[i] == 0:
        q.append(i)


stack = [0]*n

# 각 숫자 위에 몇개가 있는지 세기
# 스택리스트에 자기 위에 몇개 있는지 표시
# 연결 수 불러올때 연결수 스택에 자신 스택 +1
breaker = 0

while q :
    a = deque.popleft(q)     
    
    for i in links[a]:
        ind[i] -= 1
        stack[i] += 1+stack[a]
        if ind[i] ==0:
            q.append(i)
        elif ind[i] < 0:
            breaker = 1
            exit(0)

# ind가 0이 아니면 순환
for i in ind:
    if i != 0:
        breaker = 1
        break

if breaker != 1:
    num_box = []
    result = [0]*n
    for i in range(n+2):
        num_box.append(i)

    for i in range(n):
        num = stack[i]+1
        while True:
            if num_box[num] ==0:
                num +=1
            else :
                break
        result[i] = num
        num_box[num] = 0

    for i in result:
        print(i,end=' ')

else :
    print(-1)

# 순서표를 만든다.
# 0번 부터 stack+1 넣음. stack+1이 사용중이면 +2 넣으면 패스
# 다음 수로 넘어감