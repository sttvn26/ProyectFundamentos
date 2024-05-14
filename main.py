import machine
import network
import socket
import time
import utime
import random

# Configuración de la conexión WiFi


# Definición de pines para LEDs y botones
led_pins = [15, 14, 13, 12, 11, 10]
button_pins = [16, 17, 18, 19, 20, 21]

leds = [machine.Pin(pin, machine.Pin.OUT) for pin in led_pins]
buttons = [machine.Pin(pin, machine.Pin.IN, machine.Pin.PULL_DOWN) for pin in button_pins]

# Contadores para los goles y las veces que el portero ha parado la bola
goles = 0
paradas = 0



def encender_leds():
    for led in leds:
        led.value(1)

def apagar_leds():
    for led in leds:
        led.value(0)

def seleccionar_posicion_portero(indice):
    if indice == 1:
        grupos = [[0, 1, 2], [1, 2, 3], [2, 3, 4]]
    elif indice == 2:
        grupos = [[0, 1], [1, 2], [2, 3]]
    elif indice == 3:
        grupos = [[0, 2, 4], [1, 3, 5], [0, 3, 5]]
    
    grupo_seleccionado = random.choice(grupos)
    
    # Apagar todos los LEDs antes de encender solo los del grupo seleccionado
    apagar_leds()
    for i in grupo_seleccionado:
        leds[i].value(1)
    
    return grupo_seleccionado

def verificar_gol(portero_pos, bola_pos):
    global s  # Declarar s como global para acceder a ella dentro de la función
    if bola_pos in portero_pos:
        print("La bola fue detenida por el portero. No es gol.")
    else:
        letra = chr(65 + bola_pos)  # Convertir el índice del botón a una letra ASCII ('A' para 0, 'B' para 1, etc.)
        print(f"Gol! Enviando letra {letra} al servidor.")
        s.send(letra.encode())  # Enviar la letra al servidor

def debounce(button):
    # Esperar un breve tiempo para asegurarse de que el botón está realmente presionado
    time.sleep_ms(50)
    return button.value()

def jugar():
    while True:
        # Seleccionar la posición del portero
        indice = random.randint(1, 3)
        print(f"Se ha seleccionado el índice AN {indice}")
        portero_pos = seleccionar_posicion_portero(indice)

        # Esperar a que la bola pase por algún botón
        gol_detectado = False  # Variable para registrar si se ha detectado un gol
        while not gol_detectado:
            for i, button in enumerate(buttons):
                if debounce(button):  # Utilizar debounce aquí
                    print(f"Bola pasó por botón {i+1}")
                    verificar_gol(portero_pos, i)
                    gol_detectado = True  # Marcar que se ha detectado un gol

# Conectar a WiFi
ssid = 'Steven'
password = 'ocpv4938'

wf = network.WLAN(network.STA_IF)

wf.active(True)

wf.connect(ssid, password)
while not wf.isconnected():
    print (".")
    utime.sleep(5)
    print(".")
    utime.sleep(1)
print(wf.ifconfig()[0])   

# Conectar al servidor
s=socket.socket()
s.connect(('192.168.67.53',2032))

jugar()
