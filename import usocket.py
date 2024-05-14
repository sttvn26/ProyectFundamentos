import socket
import re

# Función para manejar las acciones basadas en las letras recibidas
def handle_action(action):
    match action:
        case 'A':
            print("Se activó la primera paleta")
        case 'B':
            print("Se activó la segunda paleta")
        case 'C':
            print("Se activó la tercera paleta")
        case 'D':
            print("Se activó la cuarta paleta")
        case 'E':
            print("Se activó la quinta paleta")
        case 'F':
            print("Se activó la sexta paleta")
        case 'G':
            print("Se presionó el botón")
        case 'H':
            print("Se debe encender el LED de local")
        case 'I':
            print("Se debe encender el LED de visitante")
        case 'J':
            print("Se debe encender el primer LED por 3 segundos")
        case 'K':
            print("Se debe encender el segundo LED por 3 segundos")
        case 'L':
            print("Se debe encender el tercer LED por 3 segundos")
        case 'M':
            print("Se debe encender el cuarto LED por 3 segundos")
        case 'N':
            print("Se debe encender el quinto LED por 3 segundos")
        case 'O':
            print("Se debe encender el sexto LED por 3 segundos")
        case _ if re.match(r'^\d+$', action):
            level = int(action)
            print(f"Nivel del ADC: {level}")
        case _:
            print(f"Acción no reconocida: {action}")

# Configuración del socket
s = socket.socket()
s.bind(('192.168.67.53' , 2032))
s.listen(13)
print("Servidor iniciado")

# Bucle principal para aceptar conexiones y recibir datos
try:
    while True:
        (sc, addr) = s.accept()
        print(f"Conexión establecida desde {addr}")
        try:
            while True:
                data = sc.recv(1024).decode().strip()
                if not data:
                    break  # Si no hay más datos, salir del bucle interno
                print(f"Datos recibidos: {data}")
                handle_action(data)
        finally:
            sc.close()
finally:
    s.close()
    print("Fin del programa")
