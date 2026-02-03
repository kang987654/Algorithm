T = int(input())
 
for test_case in range(1, T + 1):
    N = int(input())
    n_list = list(map(int, input().split()))
    
    # 제시된 문제 기반 최소, 최대 값 설정
    mn, mx = 1000000, 1
    for i in n_list:
        if mn >= i:
            mn = i
        if mx <= i:
            mx = i
    print(f'#{test_case} {mx - mn}')