def solution(citations):
    answer = len(citations)
    citations.sort(reverse=True)
    for h in range(len(citations)):
        if citations[h] < h+1:
            answer = h
            break
    return answer