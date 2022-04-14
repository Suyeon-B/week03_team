import sys
N = int(sys.stdin.readline())
tree = {}

def order(parent , o):
    if parent == '.': return

    if o == 0: print(parent,end='') # 전위 순회
    order(tree[parent][0],o) # 왼쪽 자식
    if o == 1: print(parent, end='')  # 중위 순회
    order(tree[parent][1],o) # 오른쪽 자식
    if o == 2: print(parent, end='')  # 후위 순회


while N > 0 :
    Parent , Left , Right = sys.stdin.readline().split()
    tree[Parent] = [Left,Right]
    N -=1


order('A',0)
print()
order('A',1)
print()
order('A',2)


