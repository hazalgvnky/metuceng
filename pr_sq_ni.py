def gcd(k,n):
    i=0
    if k == 0 or n == 0 :
        return 0


    elif k ==1 or n == 1 :
        return 1


    else:

        bolenler = range(2,int((k+n)/2),-1)

        if type(k//bolenler[i]) == 0 and type(n//bolenler[i]) == 0 :

            return i

        else :
             i = i + 1
             return gcd(k,n)

print(gcd(192,72))


