import sys
import sys
sys.setrecursionlimit(10**6)
# 재귀가 어디서 도는지 궁금

N, M = map(int,input().split())

nodelist =[[]for _ in range(N+1)]

for i in range(M):
    a, b = map(int,sys.stdin.readline().split())
    nodelist[a].append(b)
    nodelist[b].append(a)

visited = [False] * (N+1)
visited2 = [False] * (N+1)

def dfs(n):
    if visited[n] == False:       
        visited[n] =True
        # for i in range(len(nodelist[n])):    
            # dfs(nodelist[n][i])
        j_list.append(n)
        for i in nodelist[n]:
            dfs(i)

# def dfs(n):
#     visited[n] = True
#     for i in nodelist[n]:
#         if visited[i] == False:
#             dfs(i)

count = 0

for j in range(1,N+1):
    j_list =[]
    dfs(j)
    if j_list :
        count += 1

print(count)