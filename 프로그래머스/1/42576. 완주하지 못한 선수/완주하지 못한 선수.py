def solution(participant, completion):
    runner = {}
    for p in participant:
        if p not in runner:
            runner[p] = 1
        else:
            runner[p] += 1
    for c in completion:
        runner[c] -= 1
    for p in participant:
        if runner[p] == 1:
            answer = p
    return answer