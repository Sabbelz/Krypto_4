"""
Aufgabe 2.a.
"""
from math import gcd


def calculate_order(array):
    """
    Berechnung der order
    """
    counter = 0
    for _ in range(len(array)):
        counter += 1
    return counter


def compute_complexity(generator, prime):
    """
    Ermittlung der Komplexität
    """
    array = set()
    for k in range(1, prime):
        array.add((generator ** k) % prime)
    print("order: ", calculate_order(array))
    avg_order = 0
    for j in range(1, prime):
        for i in range(1, prime):
            avg_order += calculate_order(array) / gcd(calculate_order(array), i * j)
    avg_order /= pow(prime - 1, 2)
    print("average order: ", avg_order)
    return avg_order


compute_complexity(13, 833)

compute_complexity(13, 863)
