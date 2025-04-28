from collections import deque

def knight_min_moves(n, x1, y1, x2, y2):
    dx = [1, 1, -1, -1, 2, 2, -2, -2]
    dy = [2, -2, 2, -2, 1, -1, 1, -1]

    visited = [[False] * (n + 1) for _ in range(n + 1)]
  
    queue = deque([(x1, y1)])
    visited[x1][y1] = True
    
    distance = [[-1] * (n + 1) for _ in range(n + 1)]
    distance[x1][y1] = 0

    while queue:
        x, y = queue.popleft()
 
        if x == x2 and y == y2:
            return distance[x][y]

        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if 1 <= nx <= n and 1 <= ny <= n and not visited[nx][ny]:
                visited[nx][ny] = True
                distance[nx][ny] = distance[x][y] + 1
                queue.append((nx, ny))
    
    return -1

n = int(input())
temp = input().split()
x1, y1, x2, y2 = map(int, temp)

print(knight_min_moves(n, x1, y1, x2, y2))
