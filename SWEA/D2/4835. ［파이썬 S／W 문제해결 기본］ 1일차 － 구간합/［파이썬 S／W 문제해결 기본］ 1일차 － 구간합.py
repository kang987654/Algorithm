T = int(input())
 
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    n_list = list(map(int, input().split()))
    
    # 초기값을 첫번째 구간합으로 설정
    mn_sum, mx_sum = sum(n_list[:M]), sum(n_list[:M])
    for i in range(len(n_list)-M+1):
        # 최소 최대 구간합의 갱신
        mn_sum = min(mn_sum, sum(n_list[i:M+i]))
        mx_sum = max(mx_sum, sum(n_list[i:M+i]))
 
    print(f'#{test_case} {mx_sum - mn_sum}')
