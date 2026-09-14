products_dictionary = {}
i = 1

while i <= 3:
    product = input("Ingrese el producto a agregar○.\n")
    price = float(input(f"Ingrese el precio de {product}.\n"))
    products_dictionary[product] = price
    i += 1
    
for product, price in products_dictionary.items():
    print(f"Product: {product} con precio: ${price}")

# Para poder printear los productos tuve que ayudarme y buscar el como se hacia, si supuse que era como implemente el for pero hice:
# for product, price in products_dictionary:
#   print(product, price)