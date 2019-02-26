aux = 1
fib = 0
init = 1

Info = "Este Script imprime una suseción Fibonacci, comenzando por el nuemro 1 hasta N que es introducido por el usuario"

print (Info)
n = int(input("Ingresa un numero: "))

#El numero a ingresar debe ser mayor a 0
if n > 0:
    while init <= n:
        #Imprime los numeros dentro de los corchetes
        print ("[{0}]".format(fib),  end=" ")
        aux += fib
        fib = aux - fib
        init += 1
    print()
else:
    print("E lnumero debe ser mayor a 0")
