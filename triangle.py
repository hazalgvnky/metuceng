def triangle(n):
    listem = []
    for i in range(0,n):
        listem = listem +[((n-i-1)*" ")+((2*i+1)*"*")]
    return listem

print ('\n'.join(triangle(5)))