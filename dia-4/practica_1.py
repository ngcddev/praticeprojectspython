name_list = []
i = 1
total_list = int(input("Ponga cuantos nombres quiere en la lista.\n"))

while i <= total_list:
    i += 1
    name_list.append(input(f"Ponga un nombre a agregar en la lista, serán solo {total_list}\n"))

for number, nombre in enumerate(name_list, start=1):
    print(f"{number, nombre}")


# Nota: Enumerate funciona de la siguiente manera, enumerate(lista la cual se aplica esto, desde el numero que empieza el conteo), para mostrar las posiciones.