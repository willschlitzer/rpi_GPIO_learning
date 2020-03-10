from time import sleep
from gpiozero import Button, LED

led = LED(17)
button = Button(2)


def onoff():
    while True:
        button.wait_for_press()
        led.on()
        sleep(2)
        led.off()

def toggle():
    while True:
        button.wait_for_press()
        led.toggle()
        sleep(0.5)

def pressRelease():
    button.when_pressed = led.on
    button.when_released = led.off
    
#toggle()
pressRelease()
#onoff()
