import sys
# recursion 에러 남 / 이유 뭘까 
# 인덱로 찾는 값을 미리 소환해두기. 재귀에서 찾을 때마다 인덱스를 검색하면 시간이 늘어남
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def fun(start, end):
    # 나뉘는 점을 찾는다.
    # 루트/ 레프트 / 라이트로 나눈다.
    if start > end:
        return


    else:
        idx= start+1
        root = num[start]

        while  idx <= end:
            if root >= num[idx]:
                idx += 1
            else :
                break
        
        fun (start+1,idx-1)
        fun (idx,end)
        print (root)

num = [] 

while True:
    try:
        n = int(input())
        num.append(n)
    except:break


fun(0,len(num)-1)