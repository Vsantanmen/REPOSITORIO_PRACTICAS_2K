import os

class PartidaAjedrez:
    def __init__(self):
        self.tablero = [
            ["♜", "♞", "♝", "♛", "♚", "♝", "♞", "♜"],
            ["♟", "♟", "♟", "♟", "♟", "♟", "♟", "♟"],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            ["♙", "♙", "♙", "♙", "♙", "♙", "♙", "♙"],
            ["♖", "♘", "♗", "♕", "♔", "♗", "♘", "♖"]
        ]
        self.nombre_fichero = ""

    def obtener_texto_tablero(self):
        lineas = []
        for fila in self.tablero:
            lineas.append("\t".join(fila))
        return "\n".join(lineas)

    def guardar_tablero_actual(self):
        modo = "a" if os.path.exists(self.nombre_fichero) else "w"
        with open(self.nombre_fichero, modo, encoding="utf-8") as f:
            if modo == "a":
                f.write("\n\n")
            f.write(self.obtener_texto_tablero())

    def mover_pieza(self, f_origen, c_origen, f_destino, c_destino):
        if 0 <= f_origen < 8 and 0 <= c_origen < 8 and 0 <= f_destino < 8 and 0 <= c_destino < 8:
            pieza = self.tablero[f_origen][c_origen]
            self.tablero[f_origen][c_origen] = " "
            self.tablero[f_destino][c_destino] = pieza
            return True
        return False

    def iniciar(self):
        self.nombre_fichero = input("Introduce el nombre del fichero para guardar la partida (ej: partida.txt): ")
        if not self.nombre_fichero.endswith(".txt"):
            self.nombre_fichero += ".txt"
        
        self.guardar_tablero_actual()
        
        while True:
            accion = input("¿Quieres hacer un movimiento (m) o terminar la partida (t)?: ").lower()
            if accion == "t":
                print("Partida finalizada y guardada.")
                break
            elif accion == "m":
                try:
                    f_orig = int(input("Fila de la pieza a mover (0-7): "))
                    c_orig = int(input("Columna de la pieza a mover (0-7): "))
                    f_dest = int(input("Fila del destino (0-7): "))
                    c_dest = int(input("Columna del destino (0-7): "))
                    
                    if self.mover_pieza(f_orig, c_orig, f_dest, c_dest):
                        self.guardar_tablero_actual()
                        print("Movimiento registrado.")
                    else:
                        print("Coordenadas fuera de rango. Inténtalo de nuevo.")
                except ValueError:
                    print("Por favor, introduce números enteros válidos.")
            else:
                print("Opción no válida.")

if __name__ == "__main__":
    juego = PartidaAjedrez()
    juego.iniciar()