MOD = 107

def modular_exponentiation(a, b, mod):
    result = 1
    a = a % mod
    while b > 0:
        if b % 2 == 1:
            result = (result * a) % mod
        a = (a * a) % mod
        b //= 2
    return result

a, b = map(int, input().split())

print(modular_exponentiation(a, b, MOD))
