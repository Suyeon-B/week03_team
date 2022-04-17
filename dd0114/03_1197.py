# k 방법
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

    # if parentp[x] != x
    #   return find_parent(parent[x])
    # return x

def union_parent(parent,a,b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a<b:
        parent[b] = a
    else : # a>b
        parent[a] = b

V, E = map(int, input().split())
parent = [0]*(V+1)

links =[] 
answer = 0

for i in range(V+1):
    parent[i] = i

for i in range(E):
    start, end, cost = map(int, input().split())
    links.append([cost,start,end])
# 튜플로 넣고 리스트로 넣고 차이는? a,b가 상수가 아닐때 소팅할수있는 방법은?
# 상수를 맥이거나 아니면 이름별로 소팅할수있는 방법. 딕셔너리 쓰면 안되는지

links.sort()

for link in links:
    cost, a, b = link
    if find_parent(parent,a) != find_parent(parent, b):
        union_parent(parent,a,b)
        answer += cost

print(parent)
print(answer)