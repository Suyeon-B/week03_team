#연산자 끼워넣기
import re
import sys
import copy

N = int(input())

number = list(map(int,input().split()))

SC = list(map(int,input().split()))

SClist = SC
count = 0
result = number[0]
maximum = -1000000
minimum = 10000000

def dfs(n):
    global count
    global result
    global maximum
    global minimum

    SClist[n] -= 1
    count += 1
    
    if n == 0:
        result += number[count]
    elif n == 1:
        result -= number[count]
    elif n == 2:
        result *= number[count]
    else : # n==3
        result //= number[count]

    if count == N-1:
        if result > maximum :
            maximum = result
        if result < minimum :
            minimum = result
        return

    for i in range(4):
        if SClist[i] > 0:
            dfs(i)

for i in range(4):
    if SC[i] > 0 :
        SClist = copy.deepcopy(SC)
        count = 0
        result = number[0]
        dfs(i)

print (maximum)
print (minimum)