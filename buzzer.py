from gpiozero import Buzzer
from time import sleep

buzzer = Buzzer(17)

def onoff():
    while True:
        buzzer.on()
        sleep(1)
        buzzer.off()
        sleep(1)

def beeper():
    buzzer.beep()

#onoff()
beeper()
