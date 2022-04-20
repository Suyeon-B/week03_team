import sys

n, m = map(int,sys.stdin.readline().split())

parent = [[] for _ in range(n+1)]
child = [[] for _ in range(n+1)]

for i in range(m):
    p, c = map(int, sys.stdin.readline().split())
    parent[c].append(p)
    child[p].append(c)


answer = [0]*n
answer[0] = 1

for i in range(2,n+1) : 
    now_p=0
    now_c= len(answer)
    for j in range(len(answer)):
        t = answer[j]
        if not now_p :
            if t in parent[i]:
                now_p = j

        if t in child[i]:
            now_c = j
            break

    for k in range(now_p+1, now_c):
        if answer[k] > i :
            for l in range(k+1,len(answer)-2,-1):
                answer[l] = answer[l-1]
            answer[k] = i

print(answer)