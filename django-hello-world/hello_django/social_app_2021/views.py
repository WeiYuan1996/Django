from django.http import HttpResponse

# Create your views here.
def index(request):
	return HttpResponse("Wish you a wonderful 2021!")