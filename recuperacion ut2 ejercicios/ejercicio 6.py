nombre = input("Introduce tu nombre: ")
sexo = input("Introduce tu sexo (H para hombre, M para mujer): ").upper()
if (sexo == 'M' and nombre[0].upper() < 'M') or (sexo == 'H' and nombre[0].upper() > 'N'):
    print("Perteneces al grupo A.") 
else:
    print("Perteneces al grupo B.") 