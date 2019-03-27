# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Coin(models.Model):
    coin_type = models.CharField(max_length=100)
    coin_count = models.DecimalField(max_digits=3,decimal_places=0)

    def __str__(self):
        return self.coin_type

    def count(self):
        return self.coin_count

   # def increase(self):
       # self.coin_count += 1
      #  self.total += 1
     #   return

    #def find_total(self):
        #return self.total

