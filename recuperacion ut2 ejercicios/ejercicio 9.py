edad = int(input("Introduce tu edad: "))
if edad < 4:
    print("La entrada es gratis")
elif 4 <= edad <= 18:
    print("El precio de la entrada es 5€")
else:
    print("El precio de la entrada es 10€") 