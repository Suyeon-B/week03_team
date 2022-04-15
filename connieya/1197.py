import sys
sys.setrecursionlimit(10 ** 8)

v, e = map(int, sys.stdin.readline().split())
parents = [i for i in range(v+1)]
ans = 0
cnt = 0


def find(a):
    if a == parents[a]:
        return a

    parents[a] = find(parents[a])
    return  parents[a]


def union(a,b):
    a = find(a)
    b = find(b)
    if a != b:
        parents[a] = b

for i in range(v):
    parents[i + 1] = i + 1

graph = []
for i in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    graph.append((c, a, b))

graph.sort()
for g in graph:
  if find(g[1]) != find(g[2]):
      ans += g[0]
      cnt +=1
      union(g[1],g[2])
  if cnt == v-1:
    break

print(ans)
