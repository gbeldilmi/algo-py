def factorial(n):
    p = 1
    for i in range(2,n+1):
        p *= i
    return p


def factorial_recursive(n): # Less efficient than the above one
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n - 1)


if __name__ == '__main__':
    print(factorial(10))
    print(factorial_recursive(10))
