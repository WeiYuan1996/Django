from .models import Article
from .forms import ImageForm
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render
from django.urls import reverse
from django.core.mail import send_mail


# Create your views here.
def index(request):
	#return HttpResponse("Hello, world!")
	#all_articles = Article.objects.all()
	#return HttpResponse(all_articles)

	latest_article_list = Article.objects.order_by('-pub_date')
	#response_list = []
	#for article in latest_article_list:
	#	response_list.append(article.title)
	#return HttpResponse(response_list)

	template = loader.get_template('covid_blog/index.html')
	context = {
		'latest_article_list': latest_article_list,
	}
	return HttpResponse(template.render(context,request))
	#context is acting as a dictionary
	
def detail(request, article_id):
	article = Article.objects.get(id=article_id)
	return HttpResponse("You're looking at article: <br> <br> %s." %article.details)

def submit_article_form(request):
	return render(request, 'covid_blog/submit_article.html', {})

def success(request):
	try:

		article = Article(title=request.POST['title'],
			details=request.POST['details'],
			pub_date=request.POST['pubdate'])
		article.save()

		if article.id is not None:
			template = loader.get_template('covid_blog/success.html')
			context = {
				"message": "Success!",
				"article_id": article.id
			}
			return HttpResponse(template.render(context, request))
		else:
			template = loader.get_template('covid_blog/success.html')
			return HttpResponse(template.render({"message": "Error!"}, request))

	except Exception as error:
		template = loader.get_template('covid_blog/success.html')
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
		return render(request, 'covid_blog/image_upload.html', context)
	else:
		image_form = ImageForm()
		return render(request, 'covid_blog/image_upload.html', {'form': image_form})

def send_mail_django(request):
	bool_value = send_mail(
			'Hello Wei',
			'I hope you are having a wonderful day!'
			'weiyuanduke@gmail.com',
			['weiyuanduke@gmail.com'],
			fail_silently=False,
	)
	return HttpResponse("Mail success code: ", bool_value)
