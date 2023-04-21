import random
from FastExponentation import *

def MillerRabin(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False

    r = 0
    d = n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    for _ in range(128):
        a = random.randint(2, n - 2)
        x = fastExponentation(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = fastExponentation(x, 2, n)
            if x == n - 1:
                break
        else:
            return False

    return True