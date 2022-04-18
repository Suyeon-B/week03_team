import heapq
import sys, collections
sys.stdin = open("BFS/input.txt",'r')
input = sys.stdin.readline

"""
1: 이동할 수 있는 칸
0: 이동할 수 없는 칸

(1, 1) -> (N, M) 으로 이동할 때 지나야 하는 최소한의 칸 수
* 항상 (N, M)으로 이동할 수 있는 경우만 주어진다.

2 ≤ N, M ≤ 100
"""

"""
IDEA

BFS 풀이
1. 큐에 1인 좌표 다 넣기
2. BFS 돌면서 인접경로로 가는 길에 +1씩 하며 distance 채우기
3. 도착 시 distance값 출력
"""

# 행 n, 열 m
n, m = map(int, input().strip().split())

# 미로 판 셋팅
maze = [input().strip() for _ in range(n)]
visited = [[False]*m for _ in range(n)]
distances = collections.defaultdict(int)

# 좌표
dx = [1, -1, 0, 0] # 동서남북 순
dy = [0, 0, 1, -1]

# BFS
def find_path(start_x, start_y):
    visited[start_x][start_y] = True
    q = [[0, (start_x, start_y)]] # [cnt, [좌표]]
    distances[str(start_x)+str(start_y)] = 1
    while q:
        temp = heapq.heappop(q)[1]
        x, y = temp[0], temp[1] # 갈 수 있는 길 좌표
        for i in range(4): # 동서남북 돌면서 다음 길 찾기
            new_x, new_y = x+dx[i], y+dy[i]
            # 새로운 좌표가 미로 안에 포함되면 & 다음 길이 갈 수 있는 길이면 & 아직 안 가본 길이면
            if 0<=new_x<n and 0<=new_y<m and maze[new_x][new_y] == '1' and not visited[new_x][new_y]:
                visited[new_x][new_y] = True
                distances[str(new_x)+str(new_y)] = distances[str(x)+str(y)]+1
                heapq.heappush(q, [distances[str(new_x)+str(new_y)],(new_x, new_y)])
                # 도착지점에 왔으면 끝낸다.
                if new_x == n-1 and new_y == m-1:
                    print(distances[str(new_x)+str(new_y)])

find_path(0, 0)