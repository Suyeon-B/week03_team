# 60점 나옴 N >1000 이상일 때 시간초과

import sys
sys.setrecursionlimit(10**6)

N = int(input())

inout = "0"+str(input())

links = [[] for _ in range(N+1)]

for i in range(N-1):
    a,b = map(int,sys.stdin.readline().split())
    links[a].append(b)
    links[b].append(a)

count =0
def dfs(n):
    global count
    visited[n] = True
    for i in links[n]:
        if not visited[i]:
            if inout[i] == '0':
                dfs(i)
            else : #inout[i] == '1':
                count += 1

for i in range(1,N+1):
    visited = [False] * (N+1)
    if inout[i] == '1' :
        dfs(i)

print (count)