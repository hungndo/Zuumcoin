#Using Python 3.7 to support Async code

#Libraries required
import math
import threading
import asyncio


import zuumcoin.control.ultrasonic
import zuumcoin.control.serialCOM
import zuumcoin.control.motor

from zuumcoin.models import Coin, Battery
from django.shortcuts import get_list_or_404

#Global variables required across all functions
CHASSIS_DIAMETER =  20.3
TOLERANCE_FRONT = 5
TOLERANCE_SIDE = 5
MOVING_SPEED = 5
isRunning = True

#The initial start function
async def StartUp():
	
	# Take 3 test side values and average them
	measureSideTot = 0
	for i in range(0, 2) :
		measureSideTot += ultrasonic.measureSide
	measureSideAvg = measureSideTot / 3

	#Check with Right US IF wall distance is less than toleranceSide. If not, 
	if not measureSideAvg < 5:
		# Make a right90
		motor.Turn(1, 90)
		# Move measureSide value minus toleranceSide
		motor.Straight(1, measureSideAvg - TOLERANCE_SIDE)
		motor.Turn(-1, 90)
	# vacuum on/off
	serialCOM.setVacuum('1')

	#Create simultaneous functions
	task = asyncio.create_task(Move())
	task2 = asyncio.create_task(Check())
	task3 = asyncio.create_task(Arduino())
	
	#waits 1 second without blocking the other function
	await asyncio.sleep(1)

#Movement signals to send to the motors, based on ultrasonic returns
async def Move():
	#while frontUS return value is greater than tolerance, drive forward
	dimensionA = 0 
	dimensionB = 0
	loopNumber = 0
	global isRunning
	#find dimensionA
	while isRunning:
		nextDistance = Check()
		if(nextDistance>300):
			motor.Straight(1, 300)
			dimensionA += 300
		else:
			motor.Straight(1, nextDistance - TOLERANCE_FRONT)
			motor.Turn(-1, 90)
			dimensionA += (nextDistance - TOLERANCE_FRONT)
		break
	#find dimensionB
	while isRunning:
		nextDistance = Check()
		#find dimensionA
		if(nextDistance>300):
			motor.Straight(1, 300)
			dimensionB += 300
		else:
			motor.Straight(1, nextDistance - TOLERANCE_FRONT)
			motor.Turn(-1, 90)
			dimensionB += (nextDistance - TOLERANCE_FRONT)
		break
	#    <---|
	# o------|
	#go to the stating position of the first loop
	motor.Straight(1,dimensionA)
	motor.Turn(-1,90)
	
	#calculate loopNumber
	if dimensionA>B:
		loopNumber = dimensionA/(2*CHASSIS_DIAMETER)
	else:
		loopNumber = dimensionB/(2*CHASSIS_DIAMETER)
		
	#circle in
	for loop in range(loopNumber):
		dimensionA -= (loop+1)*CHASSIS_DIAMETER
		if dimensionA<0:
			dimensionA = 0
		dimensionB -= (loop+1)*CHASSIS_DIAMETER
		if dimensionB<0:
			dimensionB = 0
		
		#loop
		motor.Straight(1,dimensionB)
		motor.Turn(-1,90)
		moror.Straight(1,dimensionA)
		motor.Turn(-1,90)
		motor.Straight(1,dimensionB)
		motor.Turn(-1,90)
		moror.Straight(1,dimensionA)
		motor.Turn(-1,90)
#Control over ultrasonic sensing
async def Check():
	#global isRunning
	#while isRunning:
		#Check with Right US IF wall distance is within tolerance
		#if not ultrasonic.measureSide < TOLERANCE_SIDE :
		#	print("OKEY")
			
		#Check with Front US IF it is NOT within 2cm of a wall. If it is:90 degree left turn-> check again.
		#if ultrasonic.measureFront < TOLERANCE_FRONT :
			# stop the move function to make a turn and turn it back on after turn is finished
			#isRunning = False
			#motor.Turn(-1, 90) #90left turn
			#isRunning = True
			#task = asyncio.create_task(Move())

		#waits 1 second without blocking the other function
		#await asyncio.sleep(1)
		#waits a random number of seconds 
		#await asyncio.sleep(randint(0,10))
	return ultrasonic.measureFront


#Running the manipulator
async def Arduino():
	global isRunning
	while isRunning:
		# Coin counting
		coin = get_list_or_404(Coin)
		coinCount = serialCOM.getCoinCount()
		for coin_index in range(coin.length()):
			coin[coin_index].SetCoin(coinCount[coin_index])		
		# battery percentage
		battery = get_list_or_404(Battery)
		battery[0].SetBattery(serialCOM.getBattery())

#this is needed to call a coroutine and starts the program
def TurnOn():
	asyncio.run(StartUp())
def TurnOff():
	global isRunning
	isRunning = False
	serialCOM.setVacuum('0')
	
def Pause():
	print("pause")