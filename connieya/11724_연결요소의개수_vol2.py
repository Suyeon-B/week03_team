import sys


def find(a):
    if a == parent[a]: return a
    parent[a] = find(parent[a])
    return parent[a]


def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


v, e = map(int, sys.stdin.readline().split())
ans = 0
number = [0]*(v+1)
parent = [0] * (v + 1)
for i in range(1, v + 1):
    parent[i] = i

for i in range(e):
    a, b = map(int, sys.stdin.readline().split())
    union(a, b)

for i in range(1, v + 1):
    number[find(i)] +=1


for i in range(1,v+1):
    if number[i] > 0:
        ans +=1

print(ans)
