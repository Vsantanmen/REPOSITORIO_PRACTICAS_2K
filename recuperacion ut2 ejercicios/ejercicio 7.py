renta = float(input("Introduce tu renta anual en euros: "))
if renta < 10000:
    tipo = 0.05
elif renta < 20000:   
    tipo = 0.15
elif renta < 35000:
    tipo = 0.20   
elif renta < 60000:
    tipo = 0.30
else:
    tipo = 0.45
print("El tipo impositivo que te corresponde es:", tipo * 100, "%")