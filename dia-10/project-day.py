contacts = []

def read_contacts():
    return f"La lista de contactos: {contacts}"

def add_contact():
    name = input("Nombre del contacto: ")
    tel_number = input("Número del contacto: ")
    city = input("Ciudad del contacto: ")
    try:
        contacts.append({"name": str(name).title(), "tel_number": int(tel_number), "city": str(city).title()})
        print(f"Haz agregado a: {name} con el número: {tel_number} residente de: {city}.\n")
        print(f"Tu lista de contactos ha quedado: {contacts}")
    except:
        print(f"El contacto no ha podido ser añadido, revisa su nombre, teléfono o ciudad si estan bien escritos.")
    

def update_contact():
    print(f"Lista de contactos:\n {contacts}\n")
    contact_to_edit = input(f"¿Qué contacto quieres editar?")
    encontrado = False

    for position, c in enumerate(contacts):
        if str(contact_to_edit).title() == c["name"]:
            encontrado = True
            option = input("¿Qué quieres editar?: \n1. Nombre \n| 2. Número \n| 3. Ciudad\n")
            if option == "1":
                new_name = input("Ingresa el nuevo nombre.\n")
                contacts[position]["name"] = new_name

                print(f"Haz editado el nombre de tu contacto: {contacts[position]["name"]} a {new_name}")
            elif option == "2":
                new_tel_number = input("Ingresa el nuevo teléfono.\n")
                contacts[position]["tel_number"] = new_tel_number
            
                print(f"Haz editado el nombre de tu contacto: {contacts[position]["tel_number"]} a {new_tel_number}")
            elif option == "3":
                new_city = input("Ingresa la nueva ciudad.\n")
                contacts[position]["city"] = new_city
            
                print(f"Haz editado el nombre de tu contacto: {contacts[position]["city"]} a {new_city}")
    if not encontrado:
        print("Contacto no encontrado.")       

def eliminate_contact():
    print(f"Lista de contactos:\n {contacts}\n")
    contact_to_delete = input(f"¿Qué contacto quieres eliminar?\n")
    encontrado = False

    for c in contacts:
        if str(contact_to_delete).title() == c["name"]:
            encontrado = True
            contacts.remove(c)
            print(f"Haz eliminado {contact_to_delete} de tu lista de contactos.")
    if not encontrado:
        print("Contacto no encontrado.")   

def search_contact():
    contact = input("Ingresa el nombre de tu contacto a buscar: ")
    encontrado = False

    for c in contacts:
        if str(contact).title() == c["name"]:
            encontrado = True
            print(f"Contacto: {contact} encontrado.")
    if not encontrado:
        print("Contacto no encontrado.")  

while True:
    option = input("| 1. Ver tus contactos \n| 2. Añadir contacto \n| 3. Actualizar un contacto \n| 4. Eliminar un contacto \n| 5. Buscar un contacto \n| 6. Salir \n¿Qué deseas hacer?\n")

    if option == "1":
        print(read_contacts())

    elif option == "2":
        add_contact()

    elif option == "3":
        update_contact()

    elif option == "4":
        eliminate_contact()

    elif option == "5":
        search_contact()

    elif option == "6":
        break