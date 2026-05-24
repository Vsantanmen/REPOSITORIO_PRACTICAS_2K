import sys

class VisorPartida:
    def __init__(self, ruta_fichero):
        self.ruta_fichero = ruta_fichero
        self.movimientos = []
        self.cargar_partida()

    def cargar_partida(self):
        try:
            with open(self.ruta_fichero, "r", encoding="utf-8") as f:
                contenido = f.read()
            
            bloques = contenido.strip().split("\n\n")
            for bloque in bloques:
                if bloque.strip():
                    self.movimientos.append(bloque)
        except FileNotFoundError:
            print(f"Error: El fichero '{self.ruta_fichero}' no existe.")
            sys.exit()

    def mostrar_movimiento(self, numero):
        if 0 <= numero < len(self.movimientos):
            print(f"\n--- TABLERO EN EL MOVIMIENTO {numero} ---")
            print(self.movimientos[numero])
            print("-" * 35)
        else:
            print(f"Error: El movimiento {numero} no existe. Rango disponible: 0 a {len(self.movimientos) - 1}")

if __name__ == "__main__":
    archivo = input("Introduce el nombre del fichero a leer (ej: partida-ajedrez.txt): ")
    visor = VisorPartida(archivo)
    
    try:
        num_mov = int(input(f"Introduce el número de movimiento a consultar (0 a {len(visor.movimientos) - 1}): "))
        visor.mostrar_movimiento(num_mov)
    except ValueError:
        print("Error: Debes introducir un número entero.")