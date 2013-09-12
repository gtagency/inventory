from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from checkout.models import Item, Person
from django.views.decorators.csrf import csrf_exempt
from django.forms import ModelForm 
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
	try: user = Person.objects.get(gtID=data['user'])
	except Person.DoesNotExist:
		return HttpResponse("You don't exist.", 500)
	for itm in items:
		try: item = Item.objects.get(code=itm)
		except Item.DoesNotExist: pass
		if not item.checked_out:
			item.checked_out = True
			item.owner = user
			item.save()
		else:
			item.checked_out = False
			item.save()
			
	return HttpResponse("Checked out all ur books bro")

class PersonForm(ModelForm):
	class Meta:
		model = Person
		fields = ['name', 'email', 'gtID']

def register(request):
	if request.method == 'POST':
		form = PersonForm(request.POST)
		if form.is_valid():
			person = form.save()
			return HttpResponse("Thanks bro. Or sis. Whatever.")
	else:
		form = PersonForm()
	
	return render(request, 'checkout/register.html', {
		'form':form
	})

