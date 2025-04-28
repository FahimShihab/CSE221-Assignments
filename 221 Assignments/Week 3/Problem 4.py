def mod_exponent(a, b, m):
    result = 1
    a = a % m
    while b > 0:
        if b % 2 == 1:
            result = (result * a) % m
        a = (a * a) % m
        b //= 2
    return result

def mod_inverse(x, m):
    t, new_t = 0, 1
    r, new_r = m, x
    while new_r != 0:
        quotient = r // new_r
        t, new_t = new_t, t - quotient * new_t
        r, new_r = new_r, r - quotient * new_r
    if r > 1:
        return None
    if t < 0:
        t = t + m
    return t

def solve():
    T = int(input())
    
    for _ in range(T):
        a, n, m = input().split()
        a = int(a)
        n = int(n)
        m = int(m)
        
        if a == 1:
            print(n % m)
            continue
        
        a_n_mod_m = mod_exponent(a, n, m)
        numerator = (a_n_mod_m - 1 + m) % m
        a_minus_1_mod_m = (a - 1) % m
        inv_a_minus_1 = mod_inverse(a_minus_1_mod_m, m)
        
        if inv_a_minus_1 is None:
            print(0)
            continue
        
        result = (a * numerator % m) * inv_a_minus_1 % m
        print(result)

solve()
