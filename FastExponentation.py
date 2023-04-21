def fastExponentation(base, exp, mod):
    base = int(base)
    original_exp = exp
    exp = bin(int(exp))[2:]
    powOfTwo = []
    result = 1
    c = []

    for i in range(len(exp)):
        if exp[i] != '0':
            powOfTwo.append((len(exp) - 1 - i))

    i = len(powOfTwo) - 1

    while i != -1:
        a = (base ** (2 ** powOfTwo[i])) % mod
        c.append(a)
        i -= 1

    for x in c:
        result *= x

    result = result % mod

    return result
