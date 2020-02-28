def palindromes(n):
    m = []
    for i in range(n):
        if str(i) == str(i)[::-1] and str(bin(i)[2:]) == str(bin(i)[2:])[::-1]:
             m.append(i)

    return m

print(palindromes(10))
