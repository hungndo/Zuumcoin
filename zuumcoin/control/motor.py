
# Required libraries include sys, time, and GPIO
import sys
import time
import pigpio

#15.9512cm per revolution
#2048 steps per revolution
CIRCUMFRANCE = 15.9512
STEPS_PER_REV = 2048
CM_PER_DEG = float(0.141856)
CM_PER_STEP = CIRCUMFRANCE / STEPS_PER_REV
DEG_PER_STEP = float(CM_PER_STEP / CM_PER_DEG) - 0.00045

WaitTime = 0.001

# GPIO mode and pins
  # Use BCM GPIO references instead of physical pin numbers
RightMotor = [26,20,16,19] # PINS to GPIO : 11,15,16,18 --- 17,22,23,24
LeftMotor  = [5, 6, 12, 13]



# Set all pins as output


# Define advanced sequence (shown in manufacturers datasheet)
Seq = [[1,0,0,1],
       [1,0,0,0],
       [1,1,0,0],
       [0,1,0,0],
       [0,1,1,0],
       [0,0,1,0],
       [0,0,1,1],
       [0,0,0,1]]
  
StepCount = len(Seq)  

#expects a 1 for forward -1 for reverse
#duration is in cm
def Straight(dir, distance):
	pi = pigpio.pi()
	for pin in RightMotor:
		pi.set_mode(pin, pigpio.OUTPUT)
		pi.write(pin, 0)
	for pin in LeftMotor:
		pi.set_mode(pin, pigpio.OUTPUT)
		pi.write(pin, 0)
	
	currentDistance = 0
	StepCounter = 0
	
	while currentDistance <= distance:
		for pin in range(0, 4):
			
			leftPin = LeftMotor[pin]
			rightPin = RightMotor[pin]
			if Seq[StepCounter][pin]!=0:
				pi.write(leftPin, 1)
				pi.write(rightPin, 1)
			else:
				pi.write(leftPin, 0)
				pi.write(rightPin, 0)
		
		StepCounter += dir
		if (StepCounter>=StepCount):
			StepCounter = 0
		if (StepCounter<0):
			StepCounter = StepCount+dir
		
		currentDistance += CM_PER_STEP
		time.sleep(WaitTime)
	pi.stop()
		
	
#expects a 1 cw and -1 ccw
#angle is in degrees
def Turn(dir, angle):
	GPIO.setmode(GPIO.BCM)
	for pin in RightMotor:
		GPIO.setup(pin, GPIO.OUT)
		GPIO.output(pin, False)
	for pin in LeftMotor:
		GPIO.setup(pin, GPIO.OUT)
		GPIO.output(pin, False)
		
	currentAngle = 0
	LeftStepCounter = 0
	RightStepCounter = 0
	
	while currentAngle <= angle * 2:
		for pin in range (0, 4):
			
			if Seq[LeftStepCounter][pin]!=0:
				GPIO.output(LeftMotor[pin], True)
			else:
				GPIO.output(LeftMotor[pin], False)
				
			if Seq[RightStepCounter][pin]!=0:
				GPIO.output(RightMotor[pin], True)
				
			else:
				GPIO.output(RightMotor[pin], False)
		
		LeftStepCounter += dir
		RightStepCounter -= dir
		
		if(LeftStepCounter>=StepCount):
			LeftStepCounter = 0
		if(LeftStepCounter < 0):
			LeftStepCounter = StepCount+dir
			
		if(RightStepCounter>=StepCount):
			RightStepCounter = 0
		if(RightStepCounter < 0):
			RightStepCounter = StepCount-dir

		currentAngle += DEG_PER_STEP
		time.sleep(WaitTime * 3)
		
	GPIO.cleanup()
	