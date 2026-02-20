T = int(input())

for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))

    # 문제 조건에 따른 힙 구성
    tree = [0]
    for idx, num in enumerate(nums, start=1):
        tree.append(num)
        chi = idx
        par = idx // 2
        while par > 0 and tree[par] > tree[chi]:
            tree[par], tree[chi] = tree[chi], tree[par]
            chi = par
            par = par // 2

    # 마지막 노드의 조상 노드에 저장된 정수의 합
    answer = 0
    par = N // 2
    while par > 0:
        answer += tree[par]
        par = par // 2
    
    print(f'#{tc} {answer}')
