def navi(node):
    if node == -1:	# 길없음
        return 0
    if node == 99:	# 도착
        return 1
    
    return navi(arr1[node]) or navi(arr2[node])


for _ in range(10):
    tc, N = map(int, input().split())
    ways = list(map(int, input().split()))

    # 가이드와 같이 size [100]의 정적 배열 2개를 선언
    # 출발점은 0, 도착점은 99 이므로 값이 없을 경우 -1
    arr1, arr2 = [-1]*100, [-1]*100
    for i in range(0, N*2, 2):
        if arr1[ways[i]] == -1:
            arr1[ways[i]] = ways[i+1]
        else:
            arr2[ways[i]] = ways[i+1]

    print(f'#{tc} {navi(0)}')
