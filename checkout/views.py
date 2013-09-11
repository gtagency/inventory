from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from checkout.models import Item, Person
from django.views.decorators.csrf import csrf_exempt
import json

def index(request):
	items = Item.objects.all()
	return render(request, 'checkout/index.html',{'items':items})

def get(request,id):
	try: item = Item.objects.get(code=id)
	except Item.DoesNotExist:
		return HttpResponseNotFound('Couldnt find that one bro')	
	
	str = item.__dict__
	del str['_state']
	return HttpResponse(json.dumps(str), content_type='application/json') 

@csrf_exempt
def checkout(request):
	data = json.loads(request.raw_post_data)
	items = data['items']
	user, created = Person.objects.get_or_create(gtID=data['user'])
	for itm in items:
		try: item = Item.objects.get(code=itm)
		except Item.DoesNotExist: pass
		if not item.checked_out:
			item.checked_out = True
			item.owner = user
			item.save()
		else if item.owner == user:
			item.checked_out = False
			item.save()
			
	return HttpResponse("Checked out all ur books bro")


