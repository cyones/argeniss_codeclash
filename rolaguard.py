



while True:
    try: n = int(input())
    except: break
    fc = []
    while n > 1:
        for i in range(2, n + 1):
            if n % i == 0:
                n = n // i
                fc.append(i)
                break
    fc = fc + [1] * (3 - len(fc))
    print(fc)
    ############################################################################
    # TODO: esto no anda, falta combinar factores cuando tengo más de 3 de forma
    # que se minimice el area de la caja.
    while len(fc) > 3:
        fc = sorted(fc, reverse=True)
        fc = fc[:-2] + [fc[-1] * fc[-2]]
    print(fc)
    ############################################################################
    area = 2 * (fc[0] * fc[1] + fc[1] * fc[2] + fc[2] * fc[0])
    print(area)
