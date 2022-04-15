A = [50,30,24,5,28,45,98,52,60]

class Node:
    def __init__(self, item, left, right):
        self.item = item
        self.left = left
        self.right = right

tree= {}

for i in range(len(A)) :
    tree[i] = Node(key=i)
    if i > 0 :
        if tree[i] < tree[i-1] :
            tree[i].right = tree[i-1]
            tree[i-1].left = tree[i]

        while tree[i] > tree[i-1] :
            j = 1
            if tree[i] < tree[i-1-j] :
                tree[i-1-j].left = 
            else :
                j +=1