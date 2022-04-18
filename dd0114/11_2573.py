import sys

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
    
    ice[a][b] -= meltpoint
    
    if ice[a][b] < 0 :
        ice[a][b] = 0

year = 0
while True :
    breaker = 0
    for ii in range(1,n-1):
        if breaker ==1 or breaker ==2 :
            break
        
        for jj in range(1,m-1):
            if ice[ii][jj]:
                
                # 비지티드 만들기
                visited = [([0]*m) for _ in range(n)]
                for i in range(1,n-1):
                    for j in range(1,m-1):
                        if ice[i][j] :
                            visited[i][j] = 1
                #멜트 시작
                melt(ii,jj)
                
                year +=1
                
                if visited != blank :
                    breaker =2
                    print(year)
                    break
                    
                breaker = 1
                break
                
    if blank == ice :
        print (0)
        break

    if breaker ==2 :
        break


#     # if 상에 있으면
#      # 방문 안했으면
#       melt 상
#      #방문 여부와 상관없이 녹인다.
    
#     # 상하 좌우모두

# while ice 남아있으면 :
#     비지티드 초기화    
# # for문으로 나오면 def 시작
    
#         visted 1 이면 끝

