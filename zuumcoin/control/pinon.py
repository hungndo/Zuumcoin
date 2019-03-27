import RPi.GPIO as GPIO
PIN = 2
def turn_on():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PIN, GPIO.OUT)
    GPIO.output(PIN, True)