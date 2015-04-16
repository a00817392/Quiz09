print ("Distancia")
def square(n):
    x = n/2
    y = x + 1
    while (x!=y):
        z = n/x
        y = x
        x = (x + z) / 2
    return x
def hipo(x1,x2,y1,y2):
    a = (x2 - x1)
    b = (y2 - y1)
    x = (a*a) + (b*b)
    y = square(x)
    return y


x1 = int(input("Intoduce la posicion de x1 del triangulo:"))
x2 = int(input("Introduce la posicion de x2 del triangulo:"))
y1 = int(input("Introduce la posicion de y1 del triangulo:"))
y2 = int(input("Introduce la posicion de y2 del triangulo:"))

print(hipo(x1,x2,y1,y2))
