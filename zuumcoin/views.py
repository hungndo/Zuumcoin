# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import get_list_or_404
from .models import Coin
import control.control
# Create your views here.


def user_interface(request, test = 0):
    coin = get_list_or_404(Coin)
    return render(request,'zuumcoin/userInterface.html',
                  {'penny_count': coin[0].count(),
                   'nickel_count': coin[1].count(),
                   'dime_count': coin[2].count(),
                   'quarter_count': coin[3].count(),
                   'test': test
                   })

def switch(request):
    option = request.POST['choice']
    control.turn_on()
    if option == 'start':
        control.turn_on()
    else:
        control.turn_on()
    return HttpResponseRedirect(reverse('zuumcoin:interface',args=option))