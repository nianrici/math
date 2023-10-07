#!/usr/bin/env python3

import sympy as sym


def lagrange(x, y):
    n = len(x)
    poly = 0
    for i in range(n):
        num = y[i]
        den = 1
        for j in range(n):
            if i != j:
                num *= x[i] - x[j]
                den *= x[i] - x[j]
        poly += num/den
    return poly


def main():
    x = [1, 2, 3, 4]
    y = [3, 2, 0, 1]

    poly = lagrange(x, y)

    interpol = x + 1  # punto a interpolar

    L = poly.subs(x, interpol)

    print(L)


if __name__ == '__main__':
    main()

