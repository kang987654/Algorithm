import sys
from collections import deque

T = int(sys.stdin.readline())

for _ in range(T):
    inputs = sys.stdin.readline().strip()

    left = deque()
    right = deque()

    for i in inputs:
        if i == '-':
            if left:
                left.pop()
        elif i == '<':
            if left:
                right.appendleft(left.pop())
        elif i == '>':
            if right:
                left.append(right.popleft())
        else:
            left.append(i)

    print(''.join(left + right))
