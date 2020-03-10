from gpiozero import LED
from time import sleep

# Defines GPIO 17 as the port for leds
led = LED(17)

while True:
    led.on()
    sleep(1)
    led.off()
    sleep(1)
