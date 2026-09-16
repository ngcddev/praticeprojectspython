phrase = input("Escribre una frase algo larga.\n")
letter = input("¿Qué letra quieres que se cuente en la frase?\n")

print(f'La letra: "{letter}", aparece: {phrase.count(letter)} veces en la frase: "{phrase}"')