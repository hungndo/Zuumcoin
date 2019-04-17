# Required Python libraries include GPIO and time
import time
import RPi.GPIO as GPIO
# Use BCM GPIO references

GPIO.setmode(GPIO.BCM)
FrontTrigUS = 2
FrontEchoUS = 3
SideTrigUS = 4
SideEchoUS = 17

def measureFront():
  # This function measures a distance
  GPIO.output(FrontTrigUS, True)
  time.sleep(0.00001)
  GPIO.output(FrontTrigUS, False)
  start = time.time()
  #time.sleep(0.00006)
  start = time.time()

  while GPIO.input(FrontEchoUS) == 0:
    start = time.time()

  while GPIO.input(FrontEchoUS) == 1:
    stop = time.time()

  elapsed = stop-start
  distanceFront = (elapsed * 34300)/2 # times speed of sound, divide by 2 for distance

  return distanceFront

def measureSide():
  # This function measures a distance
  GPIO.output(SideTrigUS, True)
  time.sleep(0.00001)
  GPIO.output(SideTrigUS, False)
  #start = time.time()

  while GPIO.input(SideEchoUS) == 0:
    start = time.time()

  while GPIO.input(SideEchoUS) == 1:
    stop = time.time()

  elapsed = stop-start
  distanceSide = (elapsed * 34300)/2 # times speed of sound, divide by 2 for distance

  return distanceSide


print "Ultrasonic Measurement"

# Set pins as output and input
GPIO.setup(FrontTrigUS,GPIO.OUT)  # Trigger
GPIO.setup(FrontEchoUS,GPIO.IN)      # Echo

# Set trigger to False (Low)
GPIO.output(FrontTrigUS, False)

# Wrap main content in a try block so we can
# catch the user pressing CTRL-C and run the
# GPIO cleanup function. This will also prevent
# the user seeing lots of unnecessary error
# messages.
try:

  while True:

    distance = measureFront()
    print "Distance : %.1f" % distance
    time.sleep(.1)

except KeyboardInterrupt:
  # User pressed CTRL-C
  # Reset GPIO settings
  GPIO.cleanup()