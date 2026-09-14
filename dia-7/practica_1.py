full_name = input("Ingresa tu nombre.\n")
age = int(input("Ingresa tu edad.\n"))

def getName(full_name, age):
    return f"Nombre: {str(full_name).title()} | Edad: {age}."

print(getName(full_name, age))