import sys

N = int(input())

class Node :
    def __init__(self, key,left,right):
        self.key = key
        self.left = left
        self.right = right

tree = {}

for i in range(N):
    n, l, r = map(str,input().split())
    # 트리 딕셔너리에 저장한다는 뜻인데 node가 의미하는 것은? 각 노드의 이름?
    tree[n] = Node(key=n, left=l, right= r)


def preorder(node):
    print(node, end='')
    if tree[node].left != '.':
        preorder(tree[node].left)
    if tree[node].right != '.':
        preorder(tree[node].right)

def inorder(node):
    if tree[node].left != '.':
        inorder(tree[node].left)
    print(node, end='')
    if tree[node].right != '.':
        inorder(tree[node].right)

def postorder(node) :
    if tree[node].left != '.':
        postorder(tree[node].left)
    if tree[node].right != '.':
        postorder(tree[node].right)
    print(node, end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')