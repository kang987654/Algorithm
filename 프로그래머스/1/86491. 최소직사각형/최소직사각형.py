def solution(sizes):
    garo_max, sero_max = 0, 0
    for size in sizes:
        if size[0] < size[1]:
            size[0], size[1] = size[1], size[0]
        garo_max = max(size[0], garo_max)
        sero_max = max(size[1], sero_max)
    answer = garo_max * sero_max
    return answer