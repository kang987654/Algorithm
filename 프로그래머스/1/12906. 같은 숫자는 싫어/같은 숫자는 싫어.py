def solution(arr):
    answer = []
    before = -1
    for a in arr:
        if a != before:
            answer.append(a)
            before = a
    return answer