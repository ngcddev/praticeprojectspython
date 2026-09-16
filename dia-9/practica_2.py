while True:
    word = input("Ingresa una palabra cualquiera para ver si es palindroma ó '0' para salir del programa.")
    inverse_word = word[::-1]

    if word == "0":
        break
    if inverse_word.lower() == word.lower():
        print(f"La palabra: '{word}' es igual a: '{inverse_word}', por ende es palindroma.")
    else:
        print(f"La palabra: '{word}' no es igual a: '{inverse_word}', por ende no es palindroma.")
