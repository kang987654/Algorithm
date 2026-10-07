def solution(nums):
    size = len(nums) // 2
    types = len(set(nums))
    return size if types >= size else types