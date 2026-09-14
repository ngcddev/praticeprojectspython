"""
from practica_1 import names_list

for position, x in enumerate(names_list):
    if x["age"] >= 18:
        print(f"La lista tiene las siguientes personas mayores de edad.\n")
        print(f"{position}. Nombre: {x["full_name"]} | Edad: {x["age"]}\n")
    else:
        print("No hay personas mayores de edad.")
"""

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


counter = 0
print("Mayores de edad:\n")
for position, x in enumerate(names_list, start=1):
    if x["age"] >= 18:
        print(f"{position}. Nombre: {x["full_name"]} | Edad: {x["age"]}")
        counter += 1

if counter == 0:
    print("No hay mayores de edad")