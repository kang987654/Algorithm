T = int(input())


def make_num(pl, mi, mu, di, i, num):
    global min_res, max_res

    if i == N:
        min_res = min(num, min_res)
        max_res = max(num, max_res)
        return

    if pl:
        make_num(pl-1, mi, mu, di, i+1, num + nums[i])
    if mi:
        make_num(pl, mi-1, mu, di, i+1, num - nums[i])
    if mu:
        make_num(pl, mi, mu-1, di, i+1, num * nums[i])
    if di:
        make_num(pl, mi, mu, di-1, i+1, int(num / nums[i]))


for tc in range(1, T+1):
    N = int(input())
    pl, mi, mu, di = map(int, input().split())
    nums = list(map(int, input().split()))

    min_res, max_res = float('inf'), -float('inf')
    make_num(pl, mi, mu, di, 1, nums[0])

    print(f'#{tc} {max_res - min_res}' )
