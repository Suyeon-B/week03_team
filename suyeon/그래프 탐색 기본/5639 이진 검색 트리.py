import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def postorder(left, right):
    if left > right:
        return
    mid = right+1
    # preorder 순서로 입력값이 들어오기 때문에, 
    # 잘린 리스트의 첫번째 인자는 무조건 parent(처음의 경우는 root) 노드이므로
    # left+1 부터 검사해주면 된다.
    for i in range(left+1, right+1):
        # 다음 수가 parent 노드보다 크면,
        # 직전까지의 list가 left subtree가 된다.
        # 다음 수가 새로운 parent 노드가 되고,
        # 그 뒤 list가 right subtree가 된다.
        if num_list[left] < num_list[i]:
            mid=i
            break
    postorder(left+1, mid-1)
    postorder(mid, right)
    print(num_list[left])

num_list = []
def main():
    while True:
        try:
            num = int(input().strip())
            num_list.append(num)
        except:
            break

main()
postorder(0, len(num_list)-1)

# num_list = [50, 30, 24, 5, 28, 45, 98, 52, 60]