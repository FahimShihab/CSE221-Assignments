import heapq

def find_alphabet_order(words):
    graph = {}
    in_degree = {}
    used_chars = set()

    for word in words:
        for c in word:
            used_chars.add(c)
            if c not in graph:
                graph[c] = []
            if c not in in_degree:
                in_degree[c] = 0

    for i in range(1, len(words)):
        w1, w2 = words[i - 1], words[i]
        min_len = min(len(w1), len(w2))
        found_diff = False
        for j in range(min_len):
            if w1[j] != w2[j]:
                if w2[j] not in graph[w1[j]]:
                    graph[w1[j]].append(w2[j])
                    in_degree[w2[j]] += 1
                found_diff = True
                break
        if not found_diff and len(w1) > len(w2):
            return "-1"

    heap = []
    for c in used_chars:
        if in_degree.get(c, 0) == 0:
            heapq.heappush(heap, c)

    result = []
    while heap:
        current = heapq.heappop(heap)
        result.append(current)
        for neighbor in graph.get(current, []):
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                heapq.heappush(heap, neighbor)

    if len(result) != len(used_chars):
        return "-1"

    return ''.join(result)

n = int(input())
words = [input().strip() for _ in range(n)]
print(find_alphabet_order(words))
