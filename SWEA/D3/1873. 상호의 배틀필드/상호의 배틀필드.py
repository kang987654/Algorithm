class Player:
    def __init__(self, r, c, head):
        self.r = r
        self.c = c
        # 'UDLR' = '^v<>'
        self.head = direction[head]

    def move(self, d):
        next_r = self.r + direction[d][0]
        next_c = self.c + direction[d][1]

        if 0 <= next_r < H and 0 <= next_c < W and field[next_r][next_c] == '.':
            self.r = next_r
            self.c = next_c
        self.head = d

    def shoot(self):
        bullet_r, bullet_c = self.r, self.c
        d = self.head

        next_r = bullet_r + direction[d][0]
        next_c = bullet_c + direction[d][1]
        while 0 <= next_r < H and 0 <= next_c < W:
            if field[next_r][next_c] == '*':
                field[next_r][next_c] = '.'
                break
            if field[next_r][next_c] == '#':
                break
            next_r += direction[d][0]
            next_c += direction[d][1]


direction = {
    'U': (-1, +0),
    'D': (+1, +0),
    'L': (+0, -1),
    'R': (+0, +1),
    '^': 'U',
    'v': 'D',
    '<': 'L',
    '>': 'R'
}

T = int(input())

for tc in range(1, T+1):
    H, W = map(int, input().split())
    field = [list(input()) for _ in range(H)]
    N = int(input())
    commands = input()

    for i in range(H):
        for j in range(W):
            if field[i][j] in '^v<>':
                player = Player(i, j, field[i][j])
                field[i][j] = '.'

    for c in commands:
        if c in 'UDLR':
            player.move(c)
        else:
            player.shoot()

    if player.head == 'U':
        field[player.r][player.c] = '^'
    if player.head == 'D':
        field[player.r][player.c] = 'v'
    if player.head == 'L':
        field[player.r][player.c] = '<'
    if player.head == 'R':
        field[player.r][player.c] = '>'

    print(f'#{tc}', end=' ')
    for r in range(H):
        print(''.join(field[r]))
