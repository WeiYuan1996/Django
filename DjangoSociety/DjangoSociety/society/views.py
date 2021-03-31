from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context, loader

from .models import Group
from .models import Event
from .models import People
from .models import User

from .forms import ImageForm

# Create your views here.
def index(request):
	return render(request, 'society/index.html')

def group(request):
	latest_group_list = Group.objects.all()
	template = loader.get_template('society/group.html')
	context = {
		'latest_group_list': latest_group_list,
	}
	return HttpResponse(template.render(context,request))

def detail(request, group_id):
	detailview = Group.objects.get(id=group_id)
	template = loader.get_template('society/details.html')
	context = {
		'detailview' : detailview
	}
	return HttpResponse(template.render(context,request))

def event(request):
	latest_event_list = Event.objects.all()
	template = loader.get_template('society/event.html')
	context = {
		'latest_event_list': latest_event_list,
	}
	return HttpResponse(template.render(context,request))

def detail1(request, event_id):
	detailview1 = Event.objects.get(id=event_id)
	template = loader.get_template('society/details1.html')
	context = {
		'detailview1' : detailview1
	}
	return HttpResponse(template.render(context,request))

def people(request):
	latest_people_list = People.objects.all()
	template = loader.get_template('society/people.html')
	context = {
		'latest_people_list': latest_people_list,
	}
	return HttpResponse(template.render(context,request))

def detail2(request, people_id):
	detailview2 = People.objects.get(id=people_id)
	template = loader.get_template('society/details2.html')
	context = {
		'detailview2' : detailview2
	}
	return HttpResponse(template.render(context,request))


def success(request):
	try:

		people = People(about_me=request.POST['about_me'],
			birth_date=request.POST['birth_date'],
			fav_movies=request.POST['fav_movies'],
			first_name=request.POST['first_name'],
			last_name=request.POST['last_name'],
			username=request.POST['username'],
			photo_url=request.POST['photo_url'])
		people.save()

		if people.id is not None:
			template = loader.get_template('society/success.html')
			context = {
				"message": "Success!",
				"people_id": people.id
			}
			return HttpResponse(template.render(context, request))
		else:
			template = loader.get_template('society/success.html')
			return HttpResponse(template.render({"message": "Error!"}, request))

	except Exception as error:
		template = loader.get_template('society/success.html')
		return HttpResponse(template.render({"message": "Error!"}. request))


def upload_image(request):
	if request.method == 'POST':
		image_form = ImageForm(request.POST, request.FILES)
		if image_form.is_valid():
			image_form.save()
		context = {
			"form": image_form,
			"img_obj": image_form.instance
		}
		return render(request, 'society/signup.html', context)
	else:
		image_form = ImageForm()
		return render(request, 'society/signup.html', {'form': image_form})

def send_mail_django(request):
	bool_value = send_mail(
			'Hello Wei',
			'I hope you are having a wonderful day!'
			'weiyuanduke@gmail.com',
			['weiyuanduke@gmail.com'],
			fail_silently=False,
	)
	return HttpResponse("Mail success code: ", bool_value)


