# Required libraries include sys, time, and GPIO
import sys
import time
import RPi.GPIO as GPIO

#15.9512cm per revolution
#2048 steps per revolution
CIRCUMFRANCE = 15.9512
STEPS_PER_REV = 2048
CM_PER_DEG = 0.141856
CM_PER_STEP = CIRCUMFRANCE / STEPS_PER_REV
DEG_PER_STEP = CM_PER_STEP / CM_PER_DEG

# GPIO mode and pins
GPIO.setmode(GPIO.BCM)  # Use BCM GPIO references instead of physical pin numbers
RightMotor = [26,19,13,6] # PINS to GPIO : 11,15,16,18 --- 17,22,23,24
LeftMotor  = [0, 1, 2, 3]

# Set all pins as output
for pin in RightMotor:
  GPIO.setup(pin, GPIO.OUT)
  GPIO.output(pin, False)
for pin in LeftMotor:
  GPIO.setup(pin, GPIO.OUT)
  GPIO.output(pin, False)

# Define advanced sequence (shown in manufacturers datasheet)
Seq = [[1,0,0,1],
       [1,0,0,0],
       [1,1,0,0],
       [0,1,0,0],
       [0,1,1,0],
       [0,0,1,0],
       [0,0,1,1],
       [0,0,0,1]]
       

#expects a 1 for forward -1 for reverse
#duration is in cm
def Straight(dir, distance):
	currentDistance = 0
	StepCounter = 0
	
	while currentDistance <= distance:
		for pin in range(0, 4):
			xpin = StepperPins[pin]
			leftPin = LeftMotor[pin]
			rightPin = rightMotor[pin]
			if Seq[StepCounter][pin]!=0:
				GPIO.output(LeftMotor[pin], True)
				GPIO.output(RightMotor[pin], True)
			else:
				GPIO.output(LeftMotor[pin], False)
				GPIO.output(RightMotor[pin], False)
		
		StepCounter += dir
		if (StepCounter>=StepCount):
			StepCounter = 0
		if (StepCounter<0):
			StepCounter = StepCount+StepDir
		
		currentDistance += CM_PER_STEP
		time.sleep(WaitTime)
		
	
#expects a 1 cw and -1 ccw
#angle is in degrees
def Turn(dir, angle):
	currentAngle = 0
	LeftStepCounter = 0
	RightStepCounter = 0
	
	while currentAngle <= angle:
		for pin in range (0, 4):
			leftPin = LeftMotor[pin]
			rightPin = RightMotor[pin]
			if Seq[LeftStepCounter][pin]!=0:
				GPIO.output(LeftMotor[pin], True)
			else:
				GPIO.output(LeftMotor[pin], False)
				
			if Seq[RightStepCounter][pin]!=0:
				GPIO.output(RightMotor[pin], True)
			else:
				GPIO.output(LeftMotor[pin], False)
		
		LeftStepCounter += dir
		RightStepCounter -= dir
		
		if(LeftStepCounter>=StepCount):
			LeftStepCounter = 0
		if(LeftStepCounter < 0):
			LeftStepCounter = StepCount+dir
			
		if(RightStepCounter>=StepCount):
			RightStepCounter = 0
		if(RightStepCounter < 0):
			RightStepCounter = StepCount+dir
			
		currentAngle += DEG_PER_STEP
		