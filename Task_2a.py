from math import gcd


def calculate_order(array):
    counter = 0
    for _ in range(len(array)):
        counter += 1
    return counter


def compute_complexity(g, p):
    array = set()
    for k in range(1, p):
        array.add((g ** k) % p)
    print("order: ", calculate_order(array))
    avg_order = 0
    for j in range(1, p):
        for i in range(1, p):
            avg_order += calculate_order(array) / gcd(calculate_order(array), i * j)
    avg_order /= pow(p - 1, 2)
    print("average order: ", avg_order)
    return avg_order


compute_complexity(13, 833)

compute_complexity(13, 863)
