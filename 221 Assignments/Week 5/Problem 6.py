R_H = input().split()
R = int(R_H[0])
H = int(R_H[1])

grid = []
for _ in range(R):
    grid.append(input())

visited = []
for _ in range(R):
    visited.append([0] * H)

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(sr, sc):
    q = [(sr, sc)]
    visited[sr][sc] = 1
    diamonds = 1 if grid[sr][sc] == 'D' else 0
    head = 0
    while head < len(q):
        r, c = q[head]
        head += 1
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < R and 0 <= nc < H:
                if not visited[nr][nc] and grid[nr][nc] != '#':
                    visited[nr][nc] = 1
                    q.append((nr, nc))
                    if grid[nr][nc] == 'D':
                        diamonds += 1
    return diamonds

max_diamonds = 0

for i in range(R):
    for j in range(H):
        if not visited[i][j] and grid[i][j] != '#':
            max_diamonds = max(max_diamonds, bfs(i, j))

print(max_diamonds)
