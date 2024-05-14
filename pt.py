from machine import Pin, ADC
import time

from machine import ADC, Pin,PWMimport time

# Definimos los pines del potenciómetro y del LED
pin_potenciometro = ADC(27)  # Pin analógico para el potenciómetro

def obtener_estado_potenciometro(valor):
    global escoje
    escoje = [1,2]
    # Mapea el valor del potenciómetro al rango deseado (1 a 3)
    if valor > 900:
        return 1  # Máximo
    elif valor < 100:
        return 3  # Mínimo
    else:
        return 2  # Medio

while True:
    # Lee el valor del potenciómetro
    valor_potenciometro = pin_potenciometro.read()

    # Obtiene el estado del potenciómetro
    estado_potenciometro = obtener_estado_potenciometro(valor_potenciometro)

    # Imprime el estado del potenciómetro
    print(estado_potenciometro)

    time.sleep_ms(100)  # Pequeña pausa para estabilizar las lecturas


pot = ADC(27)led = PWM(Pin(16))
led2 = PWM(Pin(15))
led.freq(1000)led2.freq(1000)
while True:
    lectura = pot.read_u16()
    if lectura <= 1000 and <=10000:
        escoje = [1,2]
        time.sleep_ms(200)
    elif lectura < 10000 and <=60000:
        escoje = [2,3]
        time.sleep_ms(200)
    elif lectura < 60000:
        escoje = [1,3]
        time.sleep_ms(200)
    else:
        pass