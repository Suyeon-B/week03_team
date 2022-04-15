import sys
class Node:
    def __init__(self, key):
        self.key = key
        self.parent = self.left = self.right = None

    def __str__(self):
        return str(self.key)


class Tree:
    def __init__(self, parent, left, right):
        self.parent = Node(parent)
        if left != '.':
            self.parent.left = Node(left)
        if right != '.':
            self.parent.right = Node(right)
        self.current = self.parent

    def __len__(self):
        return self.size

    def preorder(self, v):  # 노드 v와 자손 노드를 preorder로 방문하면서 출력
        if v != None:
            print(v.key, end='')
            self.preorder(v.left)
            self.preorder(v.right)

    def inorder(self, v):
        if v != None:
            self.inorder(v.left)
            print(v.key, end='')
            self.inorder(v.right)

    def postorder(self, v):
        if v != None:
            self.postorder(v.left)
            self.postorder(v.right)
            print(v.key, end='')

    def append(self, parent, left, right):
        # 새로운 노드들을 추가하기 전에, 지금 현재의 parent를 확인한다.
        # self.parent는 생성자 호출 시에만 설정되어, 항상 root값인 'A'이다.
        # 즉, 'A'부터 트리를 확인하며 parent 자리를 찾고, 
        # left, right child를 연결한다.
        self.current = self.parent 
        stack = []
        if self.current.right: # 현재의 오른쪽 자식노드가 존재하면
            stack.append(self.current.right) # 스택에 추가
        if self.current.left: # 현재의 왼쪽 자식노드가 존재하면
            stack.append(self.current.left) # 스택에 추가
        while stack: # 스택이 비어있지 않으면 반복
            self.current = stack.pop() # 현재 노드를 stack.pop()으로 설정
            if self.current.key == parent: # 스택에서 뺀 값이 우리가 찾던 parent이면
								# Left, right child 연결해주고 return
                if left != '.':
                    self.current.left = Node(left)
                if right != '.':
                    self.current.right = Node(right)
                return
						
						# 스택에서 뺀 값이 우리가 찾던 parent가 아니면 
						# 그 자식 노드들을 stack에 넣고 while문으로 확인
            if self.current.right:
                stack.append(self.current.right)
            if self.current.left:
                stack.append(self.current.left)



input = sys.stdin.readline
N = int(input().strip())
root, left, right = input().split()
T = Tree(root, left, right)
for _ in range(N-1):
    parent, left, right = input().split()
    T.append(parent, left, right)

T.preorder(T.parent)
print()
T.inorder(T.parent)
print()
T.postorder(T.parent)