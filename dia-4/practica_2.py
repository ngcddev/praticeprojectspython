number_list = []
i = 1
counter = 0
total_list = int(input("Ingresa cuantos números quieres agregar a la lista.\n"))

while i <= total_list:
    number_list.append(int(input("Ingresa los números que quieres tener en la lista.\n")))
    i += 1

for number in number_list:
    counter += number

print(f"La suma total es: {counter}")


# Nota: Para sumar los números tuve que apoyarme de la AI para recordar como sumar los numeros, tenia en cuenta poder hacer lo que hice, pero no confie en la idea y procedi a buscar que hacer.

