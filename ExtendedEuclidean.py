def extendedEuclidean(a, b):
    rk = [a, b]; qk = [0, a // b]
    x0 = [1, 0]; y0 = [0, 1]
    k = 1; n = 1

    while True:
        n += 1
        rk.append(rk[k - 1] - (rk[k] * qk[k]))
        if rk[k + 1] == 0:
            break
        qk.append(rk[k] // rk[k + 1])
        x0.append(x0[k] * qk[k] + x0[k - 1])
        y0.append(y0[k] * qk[k] + y0[k - 1])
        k += 1

    return rk[-2], (-1) ** (n - 1) * x0[-1], (-1) ** n * y0[-1]
