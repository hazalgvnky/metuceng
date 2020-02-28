def k_possible(x,y):
    n = len(x)
    k_helper(x, "", n, y)

def k_helper(x, set, n, y):

    if (y == 0):
        print(set)
        return

    elif y == 1 :
        return set

    else:
        i=0
        newset = set + x[i]
        i=i+1
        k_helper(x, newset, n, y - 1)

print(k_possible("ab",3))