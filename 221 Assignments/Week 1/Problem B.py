T = int(input())

for i in range(T):
    expression = input().replace("calculate ", "")
    result = eval(expression)
    print(f"{result:.6f}")