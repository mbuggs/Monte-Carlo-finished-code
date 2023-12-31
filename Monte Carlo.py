Python 3.11.2 (v3.11.2:878ead1ac1, Feb  7 2023, 10:02:41) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> # mc_integration.py
... 
... import numpy as np
... from random import random
... 
... 
... def MCintegrate(f, a, b, n):
...     """
...     Monte Carlo integration to estimate the integral of f from a to b.
... 
...     Parameters
...     ----------
...     f : function
...         A function that returns a float between a and b.
...     a : float
...         Lower limit of the integral.
...     b : float
...         Upper limit of the integral.
...     n : int
...         Number of random points to take in the box.
... 
...     Returns
...     -------
...     float
...         Estimated integral of f from a to b.
...     """
... 
...     x = np.linspace(a, b, num=n, endpoint=True)
...     maxF = max(f(x))
... 
...     area = 0
... 
...     for i in range(n):
...         # generate a random point in the box
...         randNoX = random() * (b - a) + a
...         randNoY = random() * maxF
... 
        if randNoY <= f(randNoX):
            area += 1

    boxArea = (b - a) * maxF
    integral = area / n * boxArea
    return integral


if __name__ == "__main__":
    # Test the MCintegrate function with f(x) = x^2 from 1 to 3
    def f(x):
        return x ** 2

    area = MCintegrate(f, 1., 3., 50)
    print("Estimated integral of f(x) = x^2 from 1 to 3:", area)


# main.py

from mc_integration import MCintegrate


def f(x):
    return x


area = MCintegrate(f, 0, 1, 500000)
