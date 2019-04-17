#Using Python 3.7 to support Async code

#Libraries required
import math
import threading
import asyncio
import motor.py
import ultrasonic.py
import photonsensor 
from zuumcoin.models import Coin, Battery
from django.shortcuts import get_list_or_404
import serialCOM
#Global variables required across all functions

tolerance = 3
i = 0
isRunning = True

#The initial start function
async def StartUp():
	# vacuum on/off
	serialCOM.setVacuum('1')

    #Create a coroutine for other functions
	task = asyncio.create_task(Move())
	task2 = asyncio.create_task(Check())
	task3 = asyncio.create_task(Arduino())
	
	#Check with Front US IF it is NOT within 2cm of a wall. If it is:90 degree left turn-> check again.
	""""""
	#Check with Right US IF wall distance 
	""""""
	#waits 1 second without blocking the other function
	await asyncio.sleep(1)
	#prints world
	print('World')
	#waits a random number of seconds
	await asyncio.sleep(randint(0,10))
	#print number i
	print(i)

#Movement signals to send to the motors, based on ultrasonic returns
async def Move():
	print("Moving")
	
#Control over ultrasonic sensing
async def Check():
"""
		180
   270  -|-  90
	     0
"""
	global isRunning
	while isRunning:
		#Check with Front US IF it is NOT within 2cm of a wall. If it is:90 degree left turn-> check again.
		#Check with Right US IF wall distance 
		#waits 1 second without blocking the other function
		await asyncio.sleep(1)
		#waits a random number of seconds
		await asyncio.sleep(randint(0,10))


#Functions required to run the manipulator
async def Arduino():
	global isRunning
	while isRunning:
		# Coin counting
		coin = get_list_or_404(Coin)
		coinCount = serialCOM.getCoinCount()
		for coin_index in range(coin.length()):
			coin[coin_index].SetCoin(coinCount[coin_index])		
		# battery percentage
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