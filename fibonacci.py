"""This script is dedicated to Fibonacci sucession"""
from time import sleep
from os import system


def FibonacciGenerator():
	"""Generator Function of Fibonacci Sucession."""
	fibonacci_sucession = [1,1] 

	while True: 

		next_number = fibonacci_sucession[-1]  + fibonacci_sucession[-2] 
		fibonacci_sucession.append(next_number)
		yield next_number


def FibonacciSucession(end):
	"""Returns a list with fibonacci sucession."""
	try:
		generator = FibonacciGenerator()
	
		fibonacci_sucession = [1,1] + [next(generator) for n in range(how_much_numbers - 2)]

		return fibonacci_sucession

	except ValueError:
		print("Introduce un numero, por favor.")
		FibonacciSucession(end)

	finally:
		system("cls")


while True:

	option = input("1)Conocer digitos de la sucesion de fibonacci\n2)Salir\n")

	if option == "1":
		how_much_numbers = int(input("Introduce cuantos digitos quieres\n"))
		print(FibonacciSucession(how_much_numbers))
		sleep(10)
		system("cls")

	elif option == "2":
		print("Adios... :^)")
		sleep(1)
		system("cls")
		break

	
	else:
		system("cls")
