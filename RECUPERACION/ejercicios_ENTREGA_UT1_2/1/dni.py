dni_completo = input("Introduce tu DNI completo (8 números y la letra): ")
numero_dni = dni_completo[:-1]
letra_dni = dni_completo[-1].upper()
print("-" * 30)
print(f"Número de DNI: {numero_dni}")
print(f"Letra del DNI: {letra_dni}")
print("-" * 30)