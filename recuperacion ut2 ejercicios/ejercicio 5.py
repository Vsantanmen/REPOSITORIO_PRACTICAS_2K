edad = int(input("Introduce tu edad: "))
ingresos = float(input("Introduce tus ingresos mensuales en euros: "))
if edad > 16 and ingresos >= 1000:
    print("Tienes que tributar.")
else:
    print("No tienes que tributar.")