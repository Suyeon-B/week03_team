import sys
sys.stdin = open("DFS/input.txt",'r')
input = sys.stdin.readline

MAX = 300

n, m = map(int, input().strip().split())

# 빙산 이차원배열 생성
iceberg = []
for i in range(n):
    line = list(map(int, input().strip().split()))
    for j in range(m):
        iceberg.append(line)

