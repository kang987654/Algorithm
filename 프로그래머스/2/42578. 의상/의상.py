def solution(clothes):
    c_box = {}
    for cloth in clothes:
        c, c_type = cloth
        if c_type in c_box:
            c_box[c_type].append(c)
        else:
            c_box[c_type] = [c]

    answer = 1
    for c_type in c_box:
        answer *= len(c_box[c_type]) + 1
    return answer - 1