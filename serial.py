#!/usr/bin/env python3
import sympy as sym
import typer
import rich

app = typer.Typer()


def lagrange(x, y):
    n = len(x)
    p = 0
    for i in range(n):
        num = y[i]
        den = 1
        for j in range(n):
            if i != j:
                num *= x[i] - x[j]
                den *= x[i] - x[j]
        p += num/den
    return p


def main():
    x = [1, 2, 3, 4]
    y = [3, 2, 0, 1]

    p = lagrange(x, y)
    poly = sym.simplify(p)
    
    interpol = int(len(x)) + 1 # Punto a interpolar
    
    L = round(poly.subs(x, interpol))

    print(L) # Imprime resultado interpolado

if __name__ == '__main__':
    app()
