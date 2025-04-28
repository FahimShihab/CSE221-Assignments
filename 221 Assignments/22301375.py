def distance(p1, p2):
    x = p1[0] - p2[0]
    y = p1[1] - p2[1]
    return (x * x + y * y) ** 0.5

def closest_pair(points):
    def recursive(x1, y1):
        n = len(x1)
        if n <= 3:
            min_d = float('inf')
            pair = (0, 0)
            for i in range(n):
                for j in range(i + 1, n):
                    d = distance(x1[i], x1[j])
                    if d < min_d:
                        min_d = d
                        pair = (x1[i][2], x1[j][2])
            return min_d, pair

        mid = n // 2
        mid_x = x1[mid][0]
        x3, x4 = x1[:mid], x1[mid:]
        y3 = [p for p in y1 if p[0] <= mid_x]
        y4 = [p for p in y1 if p[0] > mid_x]

        d1, pair1 = recursive(x3, y3)
        d2, pair2 = recursive(x4, y4)

        d = min(d1, d2)
        best_pair = pair1 if d1 <= d2 else pair2

        strip = [p for p in y1 if abs(p[0] - mid_x) < d]

        for i in range(len(strip)):
            for j in range(i + 1, min(i + 7, len(strip))):
                d_temp = distance(strip[i], strip[j])
                if d_temp < d:
                    d = d_temp
                    best_pair = (strip[i][2], strip[j][2])

        return d, best_pair

    x1 = sorted(points)
    y1 = sorted(points, key=lambda x: x[1])
    return recursive(x1, y1)

# Input
N = int(input())
points = []
for i in range(N):
    x, y = map(int, input().split())
    points.append((x, y, i + 1))

min_d, (a, b) = closest_pair(points)
if a > b:
    a, b = b, a
print(f"{a} {b} {min_d:.6f}")
