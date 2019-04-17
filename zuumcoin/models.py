# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db.models import Sum

# Create your models here.

class Coin(models.Model):
	coin_type = models.CharField(max_length=100)
	coin_count = models.DecimalField(max_digits=3,decimal_places=0)
	coin_value = models.DecimalField(max_digits=3,decimal_places=0)
	total_value = models.DecimalField(max_digits=3,decimal_places=0)
	
	def __str__(self):
		return self.coin_type

	def Count(self):
		return self.coin_count

	def Increase(self):
		self.coin_count += 1
		self.total_value += self.coin_value
	
	def SetCoin(self, new_value):
		self.total_value -= self.coin_value * self.coin_count
		self.coin_count = new_value
		self.total_value += self.coin_value * self.coin_count
		
		
	def Reset(self):
		self.coin_count = 0
		self.total_value = 0
		
	@staticmethod
	def FindTotal():
		total_dict = Coin.objects.aggregate(total=Sum('total_value'))
		return total_dict['total']

class Battery(models.Model):
	battery_percent = models.DecimalField(max_digits=3,decimal_places=2)
	def SetBattery(self, new_value):
		self.battery_percent = new_value
	def GetBattery(self):
		return self.battery_percent