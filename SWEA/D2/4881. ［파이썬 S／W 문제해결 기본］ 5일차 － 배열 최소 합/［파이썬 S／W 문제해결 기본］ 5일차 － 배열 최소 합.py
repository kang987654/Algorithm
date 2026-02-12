def dfs(row, current_sum):
    global min_sum

    # 가지치기 - 현재 합이 다른 최소 합보다 크다면 컷
    if current_sum >= min_sum:
        return

    # 마지막까지 갔다면 최소 합 갱신
    if row == N:
        min_sum = min(min_sum, current_sum)
        return

    # 백트래킹 - 가면서 체크하고 재귀 끝나면 체크한 것을 취소
    # 안하면 다른 가지에 영향을 줄 수 있음.
    for j in range(N):
        if not visited[j]:
            visited[j] = True
            dfs(row+1, current_sum + arr[row][j])
            visited[j] = False


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    min_sum = 9 * N
    visited = [False] * N
    dfs(0, 0)
    print(f'#{tc} {min_sum}')
