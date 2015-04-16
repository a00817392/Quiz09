print ("Potencia")
def superpower(n,e):
    if e == 0:
        return 1
    r = n
    for x in range (e - 1):
        r*=n
    return r
n = int(input("Introduce el valor que deseas elevar"))
e = int(input("Inteoduce a la potencia que deseas elevar"))
print (superpower(n,e))
