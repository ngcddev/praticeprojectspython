full_name = input("Ingresa tu nombre completo\n")
age = int(input("Ingresa tu edad\n"))
city = input("Ingresa tu ciudad\n")

person_dictionary = {
    "full_name": full_name.title(),
    "age": age,
    "city": city.title()
}

print(f"Nombre: {person_dictionary['full_name']}, Edad: {person_dictionary['age']}, Ciudad: {person_dictionary['city']}")
