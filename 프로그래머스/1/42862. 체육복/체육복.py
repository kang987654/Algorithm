def solution(n, lost, reserve):
    students = [0] + [1]*n
    for l in lost:
        students[l] = 0
    for r in reserve:
        students[r] = 1
    for r in sorted(reserve):
        if r in lost:
            continue
        elif r > 1 and students[r-1] == 0:
            students[r-1] += 1
        elif r < n and students[r+1] == 0:
            students[r+1] += 1
    answer = sum(students)
    return answer