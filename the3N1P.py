def the3N1P(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        c = 1
        while n > 1:
            if n % 2 == 0:
                n = n / 2.0
            else:
                n = 3 * n + 1
            c += 1
        return c