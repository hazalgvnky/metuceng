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

def max3N1P(n):
    uncu = 0
    deger = 0
    for i in range(1,n):
    	leng=the3N1P(i)
        if leng > deger:
            deger = leng
            uncu = i
    return (uncu , deger)