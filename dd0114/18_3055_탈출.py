import sys
c, rr = map(int,input().split())
# 열과 행 매우 헷갈림 r행 c열

box = []
water =[]
start = []
end = []
stone = []
visit = []
dr = [1,0,-1,0]
dl = [0,1,0,-1]
time = 0
bibeo = []

for i in range(c):
    a = list(map(str,sys.stdin.readline().strip()))
    box.append(a)
    bibeo.append([0]*rr)
    visit.append([0]*rr)

    for j in range(len(a)):
        aj = a[j] 
        if aj == '.':
            continue
        elif aj == '*':
            water.append([i,j])
            visit[i][j] = 1

        elif aj == 'X':
            stone.append([i,j])
            visit[i][j] = 1
        elif aj == 'S':
            start.append([i,j])
            bibeo[i][j] = 1
        elif aj == 'D':
            end = [i,j]
            visit[i][j] = 1

key = 0

# print('visit')
# for k in visit:
#     print(k)
# print()

while start :
    time += 1
    for i in range(len(water)):
        l,r = water.pop(0)

        for i in range(4):
            new_l = l+dl[i]
            new_r = r+dr[i]
            if 0 <= new_l < c and 0<= new_r < rr:
                if visit[new_l][new_r] == 0:
                    visit[new_l][new_r] =1 
                    water.append([new_l,new_r])

    for i in range(len(start)):
        bl,br = start.pop(0)

        for i in range(4):
            new_bl = bl+dl[i]
            new_br = br+dr[i]
            if 0<= new_bl < c and 0<= new_br < rr:
                # 동굴 도착할시
                if [new_bl,new_br] == end :
                    print(time)
                    key = 1
                    exit(0)
                
                # 비버 이동
                if visit[new_bl][new_br] == 0:
                    if bibeo[new_bl][new_br] ==0:
                        bibeo[new_bl][new_br] = 1
                        start.append([new_bl,new_br])

if key == 0:
    print("KAKTUS")
