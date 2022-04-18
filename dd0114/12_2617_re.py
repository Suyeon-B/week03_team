import sys

n, m = map(int,input().split())

links = [[] for _ in range(n+1)]
head = [1]*(n+1)
dab = [1]*(n+1)

for i in range(m):
    a, b = map(int,sys.stdin.readline().split())
    links[a].append(b)
    head[b] = 0

for i in range(1,n+1):
    for j in links[i]:
        #  
        break


def dfs(x, count, xlist):
    
    xlist += str(x)
    # 절반길이 이상이고 끝에 노드라면
    if count >= n//2+1 and links[x]==[]:
        a = count - (n//2)
        for i in range(a): 
            dab[int(xlist[i])] = 0
            dab[int(xlist[-(i+1)])] = 0

    for i in links[x]:
        # if dab[i] : 
        dfs(i,count+1,xlist)

xlist = []
for i in range(1,n+1):
    if head[i] :
        dfs(i,1,"")

ans = 0
for i in range(1,n+1):
    if not dab[i] :
        ans += 1

print(ans)

# 노드 한뱡향으로 받음
# 연결로 리스트 만듦
# 리스트 길이 n/2 넘어가면 (길- n/2)만큼 앞뒤로 답 리스트에 넣기 - 중복방지
# 답리스트 길이 출력

