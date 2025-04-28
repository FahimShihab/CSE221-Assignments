N = int(input())
trains = []

for index in range(N):
    line = input().strip()
    parts = line.split(" at ")

    before_at = parts[0].split(" will departure for ")
    train_name = before_at[0]

    time_str = parts[1]
    hh, mm = time_str.split(":")
    total_minutes = int(hh) * 60 + int(mm)

    trains.append([train_name, total_minutes, index, line])

n = len(trains)
for i in range(n - 1):
    min_index = i
    for j in range(i + 1, n):
        if trains[j][0] < trains[min_index][0]:
            min_index = j
        elif trains[j][0] == trains[min_index][0] and trains[j][1] > trains[min_index][1]:
            min_index = j

    if min_index != i:
        trains[i], trains[min_index] = trains[min_index], trains[i]

for train in trains:
    print(train[3])
