# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import get_object_or_404, get_list_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Coin
import zuumcoin.control.control
# Create your views here.


def user_interface(request):
    coin = get_list_or_404(Coin)
    return render(request,'zuumcoin/userInterface.html',
                  {'penny_count': coin[0].count(),
                   'nickel_count': coin[1].count(),
                   'dime_count': coin[2].count(),
                   'quarter_count': coin[3].count(),
                   'total' : Coin.find_total()
                   })

def switch(request):
    try:
        option = request.POST['choice']
    except(KeyError):
        coin = get_list_or_404(Coin)
        return render(request,'zuumcoin/userInterface.html',
                      {'penny_count': coin[0].count(),
                       'nickel_count': coin[1].count(),
                       'dime_count': coin[2].count(),
                       'quarter_count': coin[3].count(),
                       'total' : Coin.find_total()
                       })
    else:
        if option == 'start':
            control.turn_on()
        elif option == 'stop':
            control.turn_off()
        else:
            control.turn_off()
        return HttpResponseRedirect(reverse('zuumcoin:interface'))
