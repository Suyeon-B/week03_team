# 숫자를 기준으로 탐색할 필요가 없다고 판단,
# 연산자를 탐색하는 코드로 재작성함

import itertools
import sys, collections
from xmlrpc.client import boolean
sys.stdin = open("DFS/input.txt",'r')
sys.setrecursionlimit(10**6) # python RecursionError 방지
input = sys.stdin.readline

MIN, MAX = float('inf'), -float('inf')
result = 0

def dfs(start_node, oper):
    global MIN, MAX, cnt, result
    cnt+=1
    if cnt<=len(oper):
        visited[start_node] = True
        next = graph[start_node]
        if not visited[next]:
            result = operate(start_node, next, oper[cnt-1])
            if not result:
                return False
            dfs(next, oper)
    return result

def operate(a, b, oper):
    if oper == '+':
        return a+b
    elif oper == '-':
        return a-b
    elif oper == '*':
        return a*b
    else: # ÷
        if (a<0 and b>0) or (a>0 and b<0):
            return -(abs(a)/abs(b))
        else:
            if b != 0:
                return a/b
            else:
                return False


# 입력될 숫자의 개수
n = int(input())

# 입력된 양 옆 숫자들만 이어지도록 
graph = collections.defaultdict(int)
nodes = [0]
nodes += list(map(int, input().split()))
for i in range(1, n):
    graph[nodes[i]] += nodes[i+1]
    # graph[nodes[i+1]] += nodes[i]

# 연산자 입력받아 끼워넣을 순서 순열로 생성
num_of_oper = list(map(int, input().split()))
temp = ['+', '-', '*', '/']
oper = []
for i in range(4):
    for j in range(num_of_oper[i]):
        oper.append(temp[i])

visited = collections.defaultdict(boolean)
operator = list(itertools.permutations(oper))
cnt = 0

for oper in operator:
    if len(oper) == 1:
        result = operate(nodes[1], nodes[2], oper[0])
        MIN = MAX = result
        break
    result = dfs(graph[nodes[1]], oper)
    if result:
        if MAX < result:
            MAX = result
        if MIN > result:
            MIN = result

print(MIN)
print(MAX)