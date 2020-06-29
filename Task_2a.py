from math import gcd


def calculate_order(array):
    counter = 0
    for i in range(len(array)):
        counter += 1
    return counter


def compute_complexity(g, p):
    array = []
    for k in range(1, p):
        array.append((g ** k) % p)
    array = list(set(array))
    print("order: ", calculate_order(array))
    counter = 0
    avg_order = 0
    for j in range(1, p):
        for i in range(1, p):
            avg_order += calculate_order(array) / gcd(calculate_order(array), i * j)
            counter += 1
    avg_order /= counter
    print("average order: ", avg_order)
    return avg_order


compute_complexity(13, 833)

compute_complexity(13, 863)
