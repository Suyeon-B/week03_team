import sys
N = int(sys.stdin.readline())
tree = {}

def preorder(parent):
    if parent == '.':
        return ''

    return parent + preorder(tree[parent][0]) + preorder(tree[parent][1])

def inorder(parent):
    if parent == '.':
        return ''

    return inorder(tree[parent][0])+parent+inorder(tree[parent][1])


def postorder(parent):
    if parent == '.':
        return ''

    return postorder(tree[parent][0])+postorder(tree[parent][1])+parent

while N > 0 :
    Parent , Left , Right = sys.stdin.readline().split()
    tree[Parent] = [Left,Right]
    N -=1


print(preorder('A'))
print(inorder('A'))
print(postorder('A'))


