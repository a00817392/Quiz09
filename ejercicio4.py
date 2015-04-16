print ("Fibonacci")
def fibonacci(n):
    a, b = 0, 1
    for x in range(n):
        a, b = b, a + b
    return a
n = int(input("Introduce el numero al cual deseas usar la funcion"))
print (fibonacci(n))
