T = int(input())

for tc in range(1, T+1):
    N = int(input())
    C = list(map(int, input().split()))

    min_diff = 1000
    sizes = sorted(list(set(C)))
    # 파티션 2개 위치
    for p1 in range(1, len(sizes)-1):
        for p2 in range(p1+1, len(sizes)):
            box_s = sizes[:p1]
            box_m = sizes[p1:p2]
            box_l = sizes[p2:]

            num_s = sum([C.count(c) for c in box_s])
            num_m = sum([C.count(c) for c in box_m])
            num_l = sum([C.count(c) for c in box_l])

            if num_s > N//2 or num_m > N//2 or num_l > N//2:
                continue
            else:
                diff = max(num_s, num_m, num_l) - min(num_s, num_m, num_l)
                min_diff = min(diff, min_diff)

    if min_diff == 1000:
        min_diff = -1
    print(f'#{tc} {min_diff}')
