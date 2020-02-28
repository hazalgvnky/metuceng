def triplets(n):
    m = []
    for a in range(1, n):
        for b in range(1, n):
            w = a**2 + b**2
            s = w ** 0.5
            c = int(s)
            z = tuple(sorted([a, b, c]))
            if c < n and s == c and z not in m:
                m.append(tuple(z))
    return m

print(triplets(100))