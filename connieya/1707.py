import sys
sys.setrecursionlimit(10**6)
T = int(sys.stdin.readline())
visited = []
graph = []
Bipartite = []

def dfs(start , flag):
    visited[start] = True
    Bipartite[start] = flag
    for nxt in graph[start]:
        if visited[nxt] == False:
            dfs(nxt , flag*-1)

def isBipartiteGraph(v):
    for i in range(1,v+1):
        for nxt in graph[i]:
            if Bipartite[nxt] == Bipartite[i]: return False

    return True

while T>0:
    V,E = map(int,sys.stdin.readline().split())
    graph = [[] for _ in range(V+1)]
    visited = [False]*(V+1)
    Bipartite = [0]*(V+1)
    for i in range(E):
        a ,b = map(int,sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1,V+1):
        if visited[i] == False:
            dfs(i,1)

    if isBipartiteGraph(V) == True:
        print("YES")
    else:
        print("NO")
    T-=1