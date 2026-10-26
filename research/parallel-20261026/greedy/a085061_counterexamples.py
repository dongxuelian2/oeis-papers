#!/usr/bin/env python3
"""Finite exact certificates refuting both stated A085061 conjectures.

The certificates already occur in the displayed OEIS data; this script
independently reconstructs them from the greedy definition. It is not
a claim that the infinite greedy process or its further behavior is solved.
"""
from math import isqrt


def prime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n) + 1))


def sequence(length):
    result = [1]
    used_differences = set()
    certificate = []
    while len(result) < length:
        x = result[-1]
        p = 2
        rejected = []
        while True:
            if prime(p) and p not in used_differences:
                valid = [y for y in (x - p, x + p)
                         if y > 0 and x + y > 1 and not prime(x + y)]
                if valid:
                    y = max(valid)
                    result.append(y)
                    used_differences.add(p)
                    certificate.append((len(result) - 1, x, p, y, rejected))
                    break
                rejected.append(p)
            p += 1
    return result, certificate


def main():
    values, certificate = sequence(31)
    published = [1, 3, 6, 19, 14, 21, 4, 23, 34, 57, 86, 117,
                 158, 121, 164, 211, 264, 205, 266, 199, 270, 353,
                 426, 505, 594, 691, 590, 487, 594, 485, 598]
    assert values == published
    failures = [(n, values[n], values[n + 5]) for n in range(26)
                if values[n + 5] <= values[n]]
    assert failures[0] == (24, 594, 485)
    assert values[24] == values[28] == 594
    print("PASS exact reconstruction of first 31 official displayed terms")
    print("Conjecture 1 false: a(24)=594 > a(29)=485")
    print("Conjecture 2 false: a(24)=a(28)=594")
    print("Each row: index, predecessor, chosen smallest eligible unused prime, value, rejected smaller unused primes")
    for row in certificate:
        print(row)


if __name__ == "__main__":
    main()
