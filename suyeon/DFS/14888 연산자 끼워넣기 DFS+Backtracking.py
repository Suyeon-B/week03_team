# DFS + 백트래킹
# retry 필요
from ast import operator
import sys
sys.stdin = open("DFS/input.txt",'r')
input = sys.stdin.readline
n = int(input())
numbers = list(map(int, input().split()))
operators = list(map(int, input().split()))  # +, -, *, //

MAX, MIN = -float('inf'), float('inf')


def dfs(depth, total):
    global MAX, MIN
    if depth == n: # 숫자 끝까지 DFS 완료 시
        MAX = max(total, MAX) # 이전 결과의 maximum이 더 클 수 있으므로
        MIN = min(total, MIN) # 이전 결과의 minimum 더 작을 수 있으므로
        return

    if operators[0]:
        # 더하기 연산자를 사용했으니 하나 줄여주고,
        # 결과에는 더한 값을 반영한다.
        operators[0]-=1
        dfs(depth + 1, total + numbers[depth])
        operators[0]+=1
    if operators[1]:
        operators[1]-=1
        dfs(depth + 1, total - numbers[depth])
        operators[1]+=1
    if operators[2]:
        operators[2]-=1
        dfs(depth + 1, total * numbers[depth])
        operators[2]+=1
    if operators[3]:
        operators[3]-=1
        dfs(depth + 1, int(total / numbers[depth]))
        operators[3]+=1


dfs(1, numbers[0])
print(MAX)
print(MIN)