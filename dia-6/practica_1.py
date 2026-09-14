names_list = []
i = 1
f = int(input("Ingresa cuantas personas quieres añadir.\n"))

while i <= f:
    full_name = input("Ingresa tu nombre completo.\n")
    age = int(input("Ingresa tu edad.\n"))
    information_dictionary = {
        "full_name": full_name,
        "age": age
    }
    names_list.append(information_dictionary)
    i += 1


for position, x in enumerate(names_list, start=1):
    print(f"{position}. Nombre: {x["full_name"]} y edad: {x["age"]}.")

# Position debe ir siempre primero antes que otro argumento, presupongo que en orden en como aparecen deben estar puestos en for.