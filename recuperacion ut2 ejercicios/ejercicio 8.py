puntuacion = float(input("Introduce tu puntuación en la evaluación (0.0, 0.4, 0.6 o más): "))
if puntuacion == 0.0:
    nivel = "Inaceptable"
    dinero = 0
elif puntuacion == 0.4:
    nivel = "Aceptable"
    dinero = 2400 * puntuacion

elif puntuacion >= 0.6:
    nivel = "Meritorio"
    dinero = 2400 * puntuacion      
else:
    nivel = "Puntuación no válida"
    dinero = 0
print("Tu nivel es:", nivel)
print("Dinero que recibirás: €", dinero)
# --- IGNORE ---