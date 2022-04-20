# heapq 이용해서도 풀어보기
import sys, collections
sys.stdin = open("BFS/input.txt",'r')
input = sys.stdin.readline

"""
IDEA
1. 일단 흰색 인접노드로 간다.
2. 인접노드가 회색일 때, 그 때의 회색 카운트 값과 좌표값을 heap에 넣는다.
3. 최소 heap에서 pop 한 곳에서 부터 다시 bfs 탐색 시작
"""


# 한 줄에 들어가는 방의 수 n
n = int(input().strip())

# 방 테이블
table = [str(input().strip()) for _ in range(n)]

# 좌표 이동용
move = [(1, 0), (-1, 0), (0, 1), (0, -1)]

# path 후보들 & 바꾼 회색 방의 개수
q = collections.deque([])
ch = [[-1]*n for i in range(n)]

# bfs
def bfs():
    global change
    # 최소 힙에 좌표 넣고
    q.append((0, 0))
    ch[0][0] = 0
    # 거기서부터 heappop 시작해서
    while q:
        x, y = q.popleft()
        # 좌표 이동해보고
        for a, b in move:
            nx, ny = x+a, y+b
            # 회색 만나면 회색 카운트한 뒤 그 값과 당시 좌표값을 heappush
            if 0<=nx<n and 0<=ny<n:
                if ch[nx][ny] == -1: # 
                    if table[nx][ny] == '0': # 회색 방 갈 때
                        q.append((nx, ny))
                        ch[nx][ny] = ch[x][y] + 1
                    else:
                        ch[nx][ny] = ch[x][y]
                        q.appendleft((nx, ny))

bfs()
print(ch[n-1][n-1])