from collections import deque

for tc in range(1, 11):
    data_len, start = map(int, input().split())
    from_to = list(map(int, input().split()))

    contacts = [[] for _ in range(101)]
    called = [False] * 101
    for i in range(data_len // 2):
        contacts[from_to[2*i]].append(from_to[2*i+1])
        contacts[from_to[2*i]].sort()

    called[start] = True
    this_step = deque([start])
    next_step = []
    while this_step:
        last = this_step.popleft()

        for c in contacts[last]:
            if not called[c]:
                called[c] = True
                next_step.append(c)
        
        if not this_step:
            this_step.extend(sorted(next_step))
            next_step.clear()

    print(f'#{tc} {last}')
