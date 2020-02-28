def recaman(a):
    if a == 0:
        return 0
    elif recaman(a - 1) - a > 0 :
        return recaman(a - 1) - a
    else:
        return recaman(a - 1) + a

print(recaman(6))