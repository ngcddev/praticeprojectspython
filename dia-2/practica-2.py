num = None
num_dividend = None


num = int(input("Ingresa un número para ver si es par o impar\n"))
num_dividend = num % 2

if num_dividend == 0:
    print("El número es par")
else:
    print("El número es impar")

