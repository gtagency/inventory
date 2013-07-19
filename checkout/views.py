from django.http import HttpResponse
from django.shortcuts import render

from checkout.models import Item

def index(request):
	items = Item.objects.all()
	return render(request, 'checkout/index.html',{'items':items})
