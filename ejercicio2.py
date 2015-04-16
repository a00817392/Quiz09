print ("Triangle")
def triangle(n):
    for r in range (1, n + 1):
        for j in range (r):
            print('T', end= "")
        print ()
    for r in range (1, n + 1):
        for j in range (n - r + 1):
            print ('T', end="")
        print ()

n = int(input("Introduce el numero del cual deseas la medida del triangulo"))
h= triangle(n)
