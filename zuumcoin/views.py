# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import get_object_or_404, get_list_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Coin, Battery
import zuumcoin.control.main
# Create your views here.


def user_interface(request):
	coin = get_list_or_404(Coin)
	battery = get_list_or_404(Battery)
	return render(request,'zuumcoin/userInterface.html',
				  {'penny_count': coin[0].Count(),
				   'nickel_count': coin[1].Count(),
				   'dime_count': coin[2].Count(),
				   'quarter_count': coin[3].Count(),
				   'total' : Coin.FindTotal(),
				   'battery' : battery[0].getBattery(),
				   })

def switch(request):
	try:
		option = request.POST['choice']
	except(KeyError):
		coin = get_list_or_404(Coin)
		return render(request,'zuumcoin/userInterface.html',
					  {'penny_count': coin[0].Count(),
					   'nickel_count': coin[1].Count(),
					   'dime_count': coin[2].Count(),
					   'quarter_count': coin[3].Count(),
					   'total' : Coin.FindTotal(),
					   'battery' : battery[0].getBattery(),
					   })
	else:
		if option == 'start':
			main.TurnOn()
		elif option == 'stop':
			main.TurnOff()
		elif option == 'pause':
			main.Pause()
		else:
			print("refresh")
		return HttpResponseRedirect(reverse('zuumcoin:interface'))
