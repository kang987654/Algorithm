def solution(participant, completion):
    runner = {}
    for p in participant:
        if p in runner:
            runner[p] += 1
        else:
            runner[p] = 1
    for c in completion:
        runner[c] -= 1
    
    answer = ''
    for k, i in runner.items():
        if i == 1:
            answer = k
            break
    return answer
