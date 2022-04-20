#버그 찾는중
import sys
import copy
sys.setrecursionlimit(10**6)

n, m = map(int,input().split())

ice = []
blank = [([0]*m) for _ in range(n)]

for i in range(n):
    ice.append(list(map(int,sys.stdin.readline().split())))

def melt(a,b) :
    visited[a][b] = 0
    # 방문 체크
    meltpoint = 4
    if ice[a+1][b]:
        if visited[a+1][b]:
            melt(a+1,b)
        meltpoint -=1
    
    if ice[a][b+1]:
        if visited[a][b+1]:
            melt(a,b+1)
        meltpoint -=1
    
    if ice[a-1][b]:
        if visited[a-1][b]:
            melt(a-1,b)
        meltpoint -=1
    
    if ice[a][b-1]:
        if visited[a][b-1]:
            melt(a,b-1)
        meltpoint -=1
    
    newice[a][b] -= meltpoint
    if newice[a][b] < 0 :
        newice[a][b] = 0

year = 0

while True :
    breaker = 0

    for ii in range(1,n-1):
        if breaker ==1 :
            break
        if ice[ii] == [0]*m:
            continue

        for jj in range(1,m-1):
            if ice[ii][jj]:
                
                # 비지티드 만들기
                visited = copy.deepcopy(ice)
                newice = copy.deepcopy(ice)
                melt(ii,jj)
                ice = newice
                year +=1
                
                if visited != blank :
                    print(year-1)
                    exit()
                   
                breaker = 1
                break
                
    if blank == ice :
        print (0)
        break
