from gpiozero import DistanceSensor
ultrasonic = DistanceSensor(echo=17, trigger=4, threshold_distance=0.5)

def waitingrange():
    while True:
        ultrasonic.wait_for_in_range()
        print("In range")
        ultrasonic.wait_for_out_of_range()
        print("Out of range")

def hello():
    print("Hello")

def bye():
    print("Bye")

def printrange():
    ultrasonic.when_in_range = hello
    ultrasonic.when_out_of_range = bye

printrange()
