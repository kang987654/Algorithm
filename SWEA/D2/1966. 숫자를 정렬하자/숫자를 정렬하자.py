def bubble_sort(nums):
    for i in range(1, len(nums)):
        for j in range(len(nums)-i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return ' '.join(map(str, nums))

def select_sort(nums):
    for i in range(0, len(nums)-1):
        min_i = i
        for j in range(i+1, len(nums)):
            if nums[min_i] > nums[j]:
                min_i = j
        nums[i], nums[min_i] = nums[min_i], nums[i]
    return ' '.join(map(str, nums))

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))

    print(f'#{tc} {bubble_sort(nums[:])}')
    # print(f'#{tc} {select_sort(nums[:])}')