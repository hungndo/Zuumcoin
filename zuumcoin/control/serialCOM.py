#this can be sotred in ~/HonorProject/I2C/serialCOM.py if not let me know

import serial
import time

#decalre the serial object as ser
ser = serial.Serial('/dev/serial0', 9600)

#we shouldn't send any mroe than 16 bytes are a time, anyhting over 16 byte the arduino wont read
CHAR_BUFFER = 16

#assign the commands to be sent to the arduino
COIN_CMD = 'C'
RESET_CMD = 'R'
VACUUM_CMD = 'V'
BATTERY_CMD = 'B'
RAWDATA_CMD = 'Z'

ACK_CMD = 'A'

def getCoinCount():
	if(ser.is_open == False):
		ser.open()
	ser.write(COIN_CMD)
	time.sleep(0.01)
	quarters = int(ser.read(2))
	dimes = int(ser.read(2))
	nickels = int(ser.read(2))
	pennies = int(ser.read(2))
	coinCount = [pennies, nickels, dimes, quarters]
	ser.close()
	return coinCount
	
	
	
def resetCoinCount():
	if(ser.is_open == False):
		ser.open()
	ser.write(RESET_CMD)
	time.sleep(0.01)
	ack = ser.read(1)
	ser.close()
	if(ack == ACK_CMD):
		return True
	else:
		return False
		
		
		
def setVacuum(state):
	if(ser.is_open == False):
		ser.open()
	ser.write(VACUUM_CMD)
	ser.write(state)
	time.sleep(0.01)
	ack = ser.read(1)
	ser.close()
	if(ack == ACK_CMD):
		return True
	else:
		return False
	
def getBattery():
	if(ser.is_open == False):
		ser.open()
	ser.write(BATTERY_CMD)
	time.sleep(0.01)
	percentage = ser.read(2)
	ser.close()
	return int(percentage)
	
def getRawData():
	if(ser.is_open == False):
		ser.open()
	ser.write(RAWDATA_CMD)
	time.sleep(0.01)
	data = ser.read(2)
	ser.close()
	return int(data)