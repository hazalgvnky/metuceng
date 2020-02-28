a = []
i=0
def letter_pairs(x):
    global i
    if len(x)-1 == i:
        return a
    else:
        a.append(x[i]+x[i+1])
        i +=1
        return letter_pairs(x)

print(letter_pairs('hazal'))