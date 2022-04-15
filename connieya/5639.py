import sys

sys.setrecursionlimit(10 ** 6)


class Node():
    def __init__(self, num, parent=None):
        self.num = num
        self.parent = parent
        self.left, self.right = None, None


num = int(sys.stdin.readline())
root = Node(num)
stack = []
cur = root


def postorder(node):
    if node == None: return
    postorder(node.left)
    postorder(node.right)
    print(node.num)


if __name__ == "__main__":
    while True:
        try:
            num = int(sys.stdin.readline())
            if num < cur.num:
                cur.left = Node(num)
                stack.append(cur)
                cur = cur.left
            else:
                while stack:
                    if num > stack[-1].num:
                        cur = stack.pop()
                    else:
                        break
                cur.right = Node(num)
                cur = cur.right
        except:
            break

postorder(root)
