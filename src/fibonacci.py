def fibonacci(n):
    a = b = 1
    for i in range(2, n + 1):
        a, b = b, a + b
    return b


def fibonacci_recursive(n): # Less efficient than the above one
    if n == 0 or n == 1:
        return 1
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


if __name__ == '__main__':
    print(fibonacci(10))
    print(fibonacci_recursive(10))
