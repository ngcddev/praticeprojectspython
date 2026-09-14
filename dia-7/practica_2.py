i = 1 
total_list = int(input("¿Cuántos números deseas promediar?\n"))
list_to_average = []

while i <= total_list:
    number = int(input("Ingresa el número a añadir a la lista.\n"))
    list_to_average.append(number)
    i += 1


def averageList(list_to_average):
    sum_list = 0
    for x in list_to_average:
        sum_list += x
    dividend = len(list_to_average)
    result = sum_list / dividend

    return result

print(f"El promedio de la lista es: {averageList(list_to_average)}")