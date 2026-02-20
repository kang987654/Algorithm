def get_node(idx):
    if idx > N:	# 단일 노드거나 out of range
        return 0
    if tree[idx] != 0:
        return tree[idx]
	# 완전 이진 탐색에서 ch1, ch2는 2*idx, 2*idx + 1
    return get_node(idx*2) + get_node(idx*2 + 1)


T = int(input())

for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    tree = [0] * (N+1)
    for _ in range(M):
        i, v = map(int, input().split())
        tree[i] = v
        
    print(f'#{tc} {get_node(L)}')
