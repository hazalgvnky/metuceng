def isprime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def prime_factors(n):
    m = []
    for i in range(2, n+1):
        if isprime(i) and n % i == 0:
            m.append(i)
    return m