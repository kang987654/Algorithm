def find_max():
    for i in range(100, 0, -1):
        if cnt_list[i]:
            cnt_list[i] -= 1
            return i

def find_min():
    for i in range(101):
        if cnt_list[i]:
            cnt_list[i] -= 1
            return i


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    nums = map(int, input().split())

    # 카운트 정렬 활용
    cnt_list = [0] * 101    # 1~100
    for num in nums:
        cnt_list[num] += 1

    special_list = []
    for _ in range(5):
        special_list.append(find_max())
        special_list.append(find_min())

    print(f'#{tc}', *special_list)