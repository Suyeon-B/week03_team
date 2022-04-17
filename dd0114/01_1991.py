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
    print(node.key, end='')
    if node.left != '.':
        preorder(tree[node.left])
    if node.right != '.':
        preorder(tree[node.right])

def inorder(node):
    if node.left != '.':
        inorder(tree[node.left])
    print(node.key,end='')
    if node.right != '.':
        inorder(tree[node.right])

def postorder(node) :
    if node.left != '.':
        postorder(tree[node.left])
    if node.right != '.':
        postorder(tree[node.right])
    print(node.key, end='')

preorder(tree['A'])
print()
inorder(tree['A'])
print()
postorder(tree['A'])

# 질문!! none 나오는 이유는??