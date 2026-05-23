frase = input("Introduce una frase: ")
caracter_buscar = "o"

repeticiones = frase.lower().count(caracter_buscar)

print(f'En la frase que has introducido, la letra "{caracter_buscar}" se repite {repeticiones} veces')