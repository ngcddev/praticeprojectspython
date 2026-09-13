num_1 = input("Ingresa tu primer numero a sumar\n")
num_2 = input("Ingresa tu segundo numero a sumar\n")



def add(num_1, num_2):
    result = int(num_1) + int(num_2)
    return result

print(f"Tu resultado es: {add(num_1, num_2)}")