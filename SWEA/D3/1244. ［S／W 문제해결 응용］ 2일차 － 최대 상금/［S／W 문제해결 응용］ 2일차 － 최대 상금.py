T = int(input())


def set_money(cnt):
    global max_money

    # 최종값 계산
    if cnt == changes:
        max_money = max(max_money, int(''.join(nums)))
        return

    # 중복값 제거
    state = ''.join(nums)
    if (state, cnt) in visited:
        return
    visited.add((state, cnt))

    for i in range(_len-1):
        for j in range(i+1, _len):
            # 백트래킹
            nums[i], nums[j] = nums[j], nums[i]
            set_money(cnt+1)
            nums[i], nums[j] = nums[j], nums[i]


for tc in range(1, T+1):
    nums, changes = input().split()
    nums = list(nums)
    changes = int(changes)

    max_money = 0
    _len = len(nums)
    visited = set()

    set_money(0)

    print(f"#{tc} {max_money}")
