def king_moves(N, x, y):
    dir = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),          (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]
    v_m = []

    for dx, dy in dir:
        new_x = x + dx
        new_y = y + dy
        if 1 <= new_x <= N and 1 <= new_y <= N:
            v_m.append((new_x, new_y))
    v_m.sort()

    print(len(v_m))
    for move in v_m:
        print(move[0], move[1])

N = int(input())
x, y = map(int, input().split())
king_moves(N, x, y)
