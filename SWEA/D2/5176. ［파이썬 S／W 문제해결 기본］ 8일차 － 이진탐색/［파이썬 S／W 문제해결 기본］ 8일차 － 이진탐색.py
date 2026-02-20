# 중위 순회 수열
def inorder(i, N):
    if i <= N:
        inorder(i*2, N)
        in_idx.append(i)
        inorder(i*2 + 1, N)


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    
    nums = list(range(N+1))
    in_idx = [0]
    inorder(1, N)

    # 1~N 으로 구성된 리스트를
    # 중위 순회 수열을 인덱스로 하는 리스트로 재배열
    btree = [(idx, num) for idx, num in zip(in_idx, nums)]
    btree.sort(key=lambda tree: tree[0])

    print(f'#{tc} {btree[1][1]} {btree[N//2][1]}')
