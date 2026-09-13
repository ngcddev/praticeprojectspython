age = None

age = input("Ingresa tu edad.\n")

if int(age) >= 18:
    print("Eres mayor de edad.")
elif 0 <= int(age) <= 18:
    print("Eres menor de edad.")
else:
    print("La edad no es posible de calcular, prueba con un número entero.")

