class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# 후위 순회식 계산
def cal_intree(node):
    v = node.value

    if v in '+-*/':
        a = cal_intree(node.left)
        b = cal_intree(node.right)

        if v == '+':
            return a + b
        if v == '-':
            return a - b
        if v == '*':
            return a * b
        if v == '/':
            return a // b
    else:
        return int(v)


for tc in range(1, 11):
    N = int(input())
    nodes = [list(input().split()) for _ in range(N)]

    # 트리 구축
    tree = [None] * (N+1)
    for node in nodes:
        i, v = int(node[0]), node[1]
        tree[i] = Node(v)
    for node in nodes:
        if len(node) == 4:
            i, _, l, r = int(node[0]), node[1], int(node[2]), int(node[3])
            tree[i].left = tree[l]
            tree[i].right = tree[r]

    print(f'#{tc} {cal_intree(tree[1])}')
