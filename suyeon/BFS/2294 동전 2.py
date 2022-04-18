import sys, collections
from collections import deque
sys.stdin = open("BFS/input.txt",'r')
input = sys.stdin.readline

"""
최소한의 동전 갯수로 k원 만들기

주의
1. 가치가 같은 동전이 여러 번 주어질 수 있음.
2. 사용한 동전의 구성이 같은데, 순서만 다르면 같은 것으로 침.

IDEA
    동전 개수만큼 정점이 있을 때, 
    각 정점의 값을 BFS로 더해 k와 같아지는 지점에서 
    들른 정점의 개수(동전의 개수)를 cnt에 담은 뒤, 
    BFS를 마치고 cnt를 출력한다.
"""
# n가지 종류의 동전, 가치의 합 k원 
# 최소한의 동전 갯수로 k원 만들기
n, k = map(int, input().strip().split())

# 코인 리스트
# 중복된 코인을 넣느니 큰 가치의 동전을 하나 넣는 게 더 나으므로,
# set으로 중복 제거, 빠르게 bfs 탈출을 위해 sort
coins = list(set(int(input().strip()) for i in range(n)))
num_of_coins = len(coins)
coins.sort()

# 이미 계산한 값은 방문 처리
visited = [0] * ((10**5)+1)

# BFS
def make_k(): 
    cnt = 1
    # 큐 변수 : [(누적 가치)]
    q = deque()
    for i in range(num_of_coins):
        q.append(coins[i])
        visited[coins[i]] = 1
    while q:
        for i in range(len(q)): # BFS인데 레벨 탐색 필요할 때
            now = q.popleft()
            for j in range(num_of_coins):
                alt = now + coins[j]
                if visited[alt] != 1:
                    if alt < k:
                        q.append(alt)
                        visited[alt] = 1
                if alt == k: # 목표 가치 달성 시
                    return cnt+1
        cnt+=1
    return -1

print(make_k())