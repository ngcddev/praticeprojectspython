while True:
    value = input("Ingresa un valor para verificar si es númerico o no.\n")
    print("Escribe: Salir para terminar el programa")
    if value == "Salir" or value == "salir":
            break 
    try:
        print(f"Tu valor si es númerico, es: {int(value)}.")
    except:
        print(f"Tu valor no es númerico, es: {value}")

