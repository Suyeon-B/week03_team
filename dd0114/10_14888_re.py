
import sys
N = int(input())
Alist = []

Alist= list(map(int,sys.stdin.readline().split()))

sclist = list(map(int,input().split()))

maximum = -10**8
minimum = 10 **8

def div(a,b):
    if a == 0:
        return 0
    elif a > 0 :
        return a//b
    else :
        return (abs(a)//b) *-1

def dfs(result, count, plus, minus, multi, divis):
    global maximum
    global minimum

    if count == N:
        if result > maximum :
            maximum = result
        if result < minimum :
            minimum = result
        return
    
    if plus > 0:
        dfs(result+Alist[count],count+1,plus-1,minus,multi,divis)
    if minus > 0:
        dfs(result-Alist[count], count+1,plus, minus-1,multi,divis)
    if multi > 0:
        dfs(result*Alist[count], count+1,plus, minus, multi-1,divis)
    if divis > 0:
        dfs((div(result,Alist[count])), count+1,plus, minus, multi, divis-1)
    
dfs(Alist[0],1,sclist[0],sclist[1],sclist[2],sclist[3])

print(maximum)
print(minimum)