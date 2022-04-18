# 그래프의 정점의 집합을 둘로 분할하여, 각 집합에 속한 정점끼리는 서로 인접하지 않도록 분할할 수 있을 때, 그러한 그래프를 특별히 이분 그래프 (Bipartite Graph) 라 부른다.
# 그래프가 입력으로 주어졌을 때, 이 그래프가 이분 그래프인지 아닌지 판별하는 프로그램을 작성하시오.

import sys
sys.setrecursionlimit(10**6)
k = int(input())

def dfs(n):
    visited[n] = True
    for i in links[n]:
        if not visited[i]:
            if dotlist[n] == False :
                dotlist[i] = True
            else:
                dotlist[i]= False
            dfs(i)


for _ in range(k) :
    v, e= map(int,input().split())

    visited = [False] * (v+1)
    dotlist = [False] * (v+1)
    links = [[] for _ in range(v+1)]

    
    for i in range(e):
        a, b = map(int,sys.stdin.readline().split())
        links[a].append(b)
        links[b].append(a)
    
    for i in range(1,v+1):
        if not visited[i]:
            dfs(i)

    count = 0
    breaker = False

    for i in range(1,len(links)):
        for j in links[i]:
            if dotlist[i] == dotlist[j]:
                count +=1
                breaker = True
                break        
        if breaker :
            break

    if count == 0:
        print('YES')
    else :
        print('NO')