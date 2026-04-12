dr = [-1, +0, +1, +0]
dc = [+0, +1, +0, -1]

class RC:
    def __init__(self, r, c):
        self.r = r
        self.c = c
        self.d = 0  # 0, 1, 2, 3
    
    def go(self):
        next_r = self.r + dr[self.d]
        next_c = self.c + dc[self.d]
    
        if 0 <= next_r < N and 0 <= next_c < N and park[next_r][next_c] != 'T':
            self.r = next_r
            self.c = next_c
    
    def turn(self, t):
        t = 1 if t == 'R' else -1
        self.d = (self.d+4 + t) % 4


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    park = [list(input()) for _ in range(N)]
    Q = int(input())
    commands = []
    for _ in range(Q):
        _, command = input().split()
        commands.append(command)

    for i in range(N):
        for j in range(N):
            if park[i][j] == 'X':
                sr, sc = i, j
            if park[i][j] == 'Y':
                er, ec = i, j

    answer = []
    for command in commands:
        cy = RC(sr, sc)
        for c in command:
            if c == 'A':
                cy.go()
            else:
                cy.turn(c)
        if (cy.r, cy.c) == (er, ec):
            answer.append(1)
        else:
            answer.append(0)

    print(f'#{tc}', *answer)
