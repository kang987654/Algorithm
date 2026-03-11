T = int(input())


def merge(left, right):
    global cnt

    l_idx, r_idx = 0, 0		# pop(0) 의 경우, 시간 초과!
    res = []
    while l_idx < len(left) or r_idx < len(right):
        if l_idx < len(left) and r_idx < len(right):
            if left[l_idx] <= right[r_idx]:
                res.append(left[l_idx])
                l_idx += 1
            else:
                res.append(right[r_idx])
                r_idx += 1
        elif l_idx < len(left):
            cnt += 1
            res.extend(left[l_idx:])
            break
        elif r_idx < len(right):
            res.extend(right[r_idx:])
            break

    return res


def merge_sort(arr):
    if len(arr) == 1:
        return arr

    left = merge_sort(arr[0: len(arr)//2])
    right = merge_sort(arr[len(arr)//2: N])

    return merge(left, right)


for tc in range(1, T+1):
    N = int(input())
    L = list(map(int, input().split()))

    cnt = 0
    sL = merge_sort(L)

    print(f'#{tc} {sL[N//2]} {cnt}')
