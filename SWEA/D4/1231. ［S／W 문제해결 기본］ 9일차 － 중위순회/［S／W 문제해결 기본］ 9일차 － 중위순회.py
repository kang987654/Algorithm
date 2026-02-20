class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# 중위 순회 출력
def inorder(node):
    if node:
        inorder(node.left)
        print(node.value, end='')
        inorder(node.right)


for tc in range(1, 11):
    N = int(input())
    nodes = [list(input().split()) for _ in range(N)]

    # 완전 이진 트리이므로 역순으로 트리 구축
    tree = [None] * (N+1)
    for node in nodes[::-1]:
        if len(node) == 2:
            i, v = node
            tree[int(i)] = Node(v)
        if len(node) == 3:
            i, v, l = node
            tree[int(i)] = Node(v, tree[int(l)])
        if len(node) == 4:
            i, v, l, r = node
            tree[int(i)] = Node(v, tree[int(l)], tree[int(r)])

    print(f'#{tc}', end=' ')
    inorder(tree[1])
    print()
