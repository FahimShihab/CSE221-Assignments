a = input()
b = a.split()
N = int(b[0])
M = int(b[1])

u_inp = input().split()
u = []
for val in u_inp:
    u.append(int(val))

v_inp = input().split()
v = []
for val in v_inp:
    v.append(int(val))

w_inp = input().split()
w = []
for val in w_inp:
    w.append(int(val))

adj_list = []
for i in range(N):
    adj_list.append([])

for i in range(M):
    from_node = u[i] - 1
    to_node = v[i]
    weight = w[i]
    adj_list[from_node].append((to_node, weight))

for i in range(N):
    print(str(i + 1) + ":", end='')
    for pair in adj_list[i]:
        print(" (" + str(pair[0]) + "," + str(pair[1]) + ")", end='')
    print()
