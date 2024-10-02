from django.shortcuts import render
from django.http import HttpResponse
from .signals import my_signal

def trigger_signal(request):
    # Trigger the signal
    my_signal.send(sender=None)
    return HttpResponse("Signal has been triggered!")