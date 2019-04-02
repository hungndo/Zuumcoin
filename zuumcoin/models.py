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

    def count(self):
        return self.coin_count

    def increase(self):
        self.coin_count += 1
        self.total_value += coin_value
        
    def reset(self):
        self.coin_count = 0
        self.total_value = 0
        
    @staticmethod
    def find_total():
        total_dict = Coin.objects.aggregate(total=Sum('total_value'))
        return total_dict['total']
