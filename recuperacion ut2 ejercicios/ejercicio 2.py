contrasena_guardada = "contraseña"

intento_usuario = input("Introduce la contraseña: ")

if intento_usuario.lower() == contrasena_guardada.lower():
    print("La contraseña coincide")
else:
    print("La contraseña no coincide")