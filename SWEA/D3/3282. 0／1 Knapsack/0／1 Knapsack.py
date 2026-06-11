T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    
    # dp[i]는 부피가 i일 때의 최대 가치
    dp = [0] * (K + 1)
    
    for _ in range(N):
        v, c = map(int, input().split())
        # 각 물건은 한 번만 넣을 수 있으므로 뒤에서부터 갱신 (0-1 배낭 문제)
        for j in range(K, v - 1, -1):
            dp[j] = max(dp[j], dp[j - v] + c)
            
    print(f'#{tc} {dp[K]}')
