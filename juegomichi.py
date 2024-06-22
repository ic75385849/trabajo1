def dibujar_tablero(tablero):
    print("  1   2   3")
    print(f"1 {tablero[0][0]} | {tablero[0][1]} | {tablero[0][2]} ")
    print(" ---|---|---")
    print(f"2 {tablero[1][0]} | {tablero[1][1]} | {tablero[1][2]} ")
    print(" ---|---|---")
    print(f"3 {tablero[2][0]} | {tablero[2][1]} | {tablero[2][2]} ")

def verificar_ganador(tablero, jugador):
    # Verificar filas
    for fila in tablero:
        if all([casilla == jugador for casilla in fila]):
            return True
    
    # Verificar columnas
    for col in range(3):
        if all([tablero[fil][col] == jugador for fil in range(3)]):
            return True
    
    # Verificar diagonales
    if all([tablero[i][i] == jugador for i in range(3)]) or \
       all([tablero[i][2-i] == jugador for i in range(3)]):
        return True
    
    return False

def jugar_michi():
    tablero = [[' ' for _ in range(3)] for _ in range(3)]
    jugadores = ['X', 'O']
    jugador_actual = 0
    jugadas_disponibles = 9
    
    while True:
        dibujar_tablero(tablero)
        
        # Turno del jugador
        print(f"Turno del jugador {jugadores[jugador_actual]}")
        fila = int(input("Ingrese el número de fila (1-3): ")) - 1
        columna = int(input("Ingrese el número de columna (1-3): ")) - 1
        
        # Verificar si la casilla está ocupada
        if tablero[fila][columna] != ' ':
            print("¡Casilla ocupada! Intente de nuevo.")
            continue
        
        # Marcar la casilla
        tablero[fila][columna] = jugadores[jugador_actual]
        jugadas_disponibles -= 1
        
        # Verificar si hay un ganador
        if verificar_ganador(tablero, jugadores[jugador_actual]):
            dibujar_tablero(tablero)
            print(f"¡Jugador {jugadores[jugador_actual]} ha ganado!")
            break
        
        # Verificar empate
        if jugadas_disponibles == 0:
            dibujar_tablero(tablero)
            print("¡Empate!")
            break
        
        # Cambiar al siguiente jugador
        jugador_actual = 1 - jugador_actual

if __name__ == "__main__":
    print("Bienvenido al juego Michi (Tres en Raya)!")
    jugar_michi()
