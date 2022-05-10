from factiorial import factorial


def binomial_coefficient(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))


def binomial_coefficient_recursive(n, k): # Less efficient than the above one
    if n > k and k > 0:
        return binomial_coefficient_recursive(n - 1, k - 1) + binomial_coefficient_recursive(n - 1, k)
    return 1


if __name__ == '__main__':
    print(binomial_coefficient(10, 5))
    print(binomial_coefficient_recursive(10, 5))
