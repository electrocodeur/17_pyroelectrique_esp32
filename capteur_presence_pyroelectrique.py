from machine import Pin
import time

pir_pin = Pin(15, mode=Pin.IN)

while True:
    if pir_pin.value() == 1:
        print("Mouvement !!")
    time.sleep_ms(100)
