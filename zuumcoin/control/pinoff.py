import RPi.GPIO as GPIO
PIN = 14
def turn_off():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PIN, GPIO.OUT)
    GPIO.output(PIN, False)