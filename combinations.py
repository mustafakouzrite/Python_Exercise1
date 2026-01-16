def fact(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result


def comb(n, k):
    return fact(n) // (fact(k) * fact(n - k))
