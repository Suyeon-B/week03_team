c = int(input())
l = int(input())

line = []

for i in range(l):
    a,b = map(int,input().split())
    line.append([a,b])

parent = [0] * (c+1)

for i in range(c+1):
    parent[i] = i

def union(a,b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        b < a
        parent[a] = b

def find(a):
    if a != parent[a]:
        parent[a] = find(parent[a])
    return parent[a]

for i in range(l):
    a,b = line[i]
    union(a,b)

for i in range(l):
    a,b = line[i]
    union(a,b)

count = 0
for i in range(c+1):
    if parent[i] == 1:
        count +=1

print(count-1)