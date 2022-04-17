# 리크루젼 에러 나는 이유 찾기

import sys
sys.setrecursionlimit(10**6)

N,M = map(int,input().split())
xlist = []

for i in range(M) :
    a, b = map(int,input().split())
    xlist.append([a,b])

parlist = [0]*(N+1)

for i in range(N+1):
    parlist[i] = i

def find_parent(x):
    if parlist[x] == x:
        return x
    return find_parent(parlist[x])

    # if parlist[x] == x : return x
    # parlist[x] = find_parent(parlist[x])
    # return parlist[x]

def union(a,b) :
    a = find_parent(a)
    b = find_parent(b)
    if a < b :
        parlist[b] = a
    else: # b > a :
        parlist[a] = b

for i in range(M):
    a, b = xlist[i]
    union (a,b)

for i in range(1, N+1):
    while parlist[i] != parlist[parlist[i]]:
        parlist[i] = parlist[parlist[i]]

parlist = set(parlist)
 
print (len(parlist)-1)

