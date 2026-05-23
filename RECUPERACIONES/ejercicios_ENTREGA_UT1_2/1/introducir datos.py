registro = {}

print("--- REGISTRO DE NUEVO USUARIO ---")

registro["Nombre"] = input("Introduce el nombre: ").strip()
registro["Apellidos"] = input("Introduce los apellidos: ").strip()
registro["DNI"] = input("Introduce el DNI (con letra): ").strip().upper()
registro["Fecha de Nacimiento"] = input("Introduce la fecha de nacimiento (DD/MM/AAAA): ").strip()

print("\n" + "=" * 40)
print("         DATOS DEL REGISTRO")
print("=" * 40)

for clave, valor in registro.items():
    print(f"🔹 {clave}: {valor}")

print("=" * 40)