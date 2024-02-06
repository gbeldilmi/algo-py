def power(x, n):
    neg = n < 0
    if neg:
        n = -n
    p = 1
    for _ in range(n):
        p *= x
    if neg:
        p = 1 / p
    return p


def power_recursive(x, n): # More efficient than the above one
    if n < 0:
        return 1 / power_recursive(x, -n)
    if n == 0:
        return 1
    a = power_recursive(x, n // 2)
    if n % 2 == 0: 
        return a * a
    else:
        return a * a * x


if __name__ == '__main__':
    print(power(13, 15))
    print(power_recursive(13, 15))
