T = 10
 
for test_case in range(1, T+1):
    N = int(input())
    buildings = list(map(int, input().split()))
 
    view = 0
    for i in range(2, N-2):
        around = buildings[i-2:i] + buildings[i+1:i+3]
        if buildings[i] <= max(around):
            continue
        view += buildings[i] - max(around)
     
    print(f'#{test_case} {view}')