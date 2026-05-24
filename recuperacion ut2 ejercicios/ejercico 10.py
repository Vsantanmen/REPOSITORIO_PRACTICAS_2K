print("Bienvenido a la pizzería Bella Napoli")
tipo_pizza = input("¿Quieres una pizza vegetariana? (S/N): ").strip().upper()

ingredientes_base = "Tomate, Mozzarella"

if tipo_pizza == "S":
    es_vegetariana = "Vegetariana"
    print("\nIngredientes vegetarianos disponibles:\n1. Pimiento\n2. Tofu")
    opcion = input("Elige un ingrediente (1 o 2): ").strip()
    
    if opcion == "1":
        ingrediente_elegido = "Pimiento"
    else:
        ingrediente_elegido = "Tofu"

else:
    es_vegetariana = "No Vegetariana"
    print("\nIngredientes no vegetarianos disponibles:\n1. Peperoni\n2. Jamón\n3. Salmón")
    opcion = input("Elige un ingrediente (1, 2 o 3): ").strip()
    
    if opcion == "1":
        ingrediente_elegido = "Peperoni"
    elif opcion == "2":
        ingrediente_elegido = "Jamón"
    else:
        ingrediente_elegido = "Salmón"

print("\n" + "=" * 40)
print(f"Tipo de pizza: {es_vegetariana}")
print(f"Ingredientes: {ingredientes_base}, {ingrediente_elegido}")
print("=" * 40)