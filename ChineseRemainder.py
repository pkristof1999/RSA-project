from FastExponentation import *
from ExtendedEuclidean import *

def chineseRemainder(p, q, c, d):
    c1 = fastExponentation(c, d % (p - 1), p)
    c2 = fastExponentation(c, d % (q - 1), q)

    M1, M2 = q, p
    M = p * q
    d, y1, y2 = extendedEuclidean(M1, M2)

    return ((c1 * y1 * M1) + (c2 * y2 * M2)) % M