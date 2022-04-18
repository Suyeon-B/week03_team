# 루트 없는 트리가 주어진다. 이때, 트리의 루트를 1이라고 정했을 때, 각 노드의 부모를 구하는 프로그램을 작성하시오.

# dfs를 재귀로 소환
# 부모 노드 기록 리스트 만들기
# 새로운 dfs를 불러올때 자식 노드를 인덱스에 저장

import sys
sys.setrecursionlimit(10**6)
n = int(input())

node = [[] for _ in range(n+1)]

for i in range(n-1):
    a, b = map(int,sys.stdin.readline().split())
    node[a].append(b)
    node[b].append(a)

parent = [0]*(n+1)
visited = [False]*(n+1)


def dfs(n):
    visited[n] = True
    for i in node[n]:
        if not visited[i]:
            parent[i]=n
            dfs(i)

dfs(1)

for i in range(2,n+1):
    print(parent[i])