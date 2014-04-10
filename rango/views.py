# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from rango.models import Category
from rango.models import Page

def index(request):
    # Request the context of the request.
    # The context contains information such as the client's machine details, for example.
	context = RequestContext(request)
    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
#    context_dict = {'boldmessage': "I am bold font from the context"}
	category_list = Category.objects.order_by('-likes')[:5]
#Most viewed pages here
	page_list = Page.objects.order_by('-views')[:5]
	context_dict = {'categories': category_list, 'most_pages': page_list}
	for category in category_list:
		category.url = category.name.replace(' ', '_')
    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
	return render_to_response('rango/index.html', context_dict, context)

	#return HttpResponse("Rango says hello world! <a href='/rango/about'>About</a>")
def new(request):
	context = RequestContext(request)
	context_dict = {'newbold': "My new bold from view :)"}
	return render_to_response('rango/new.html', context_dict, context)

#def about(request):
#	return HttpResponse("Rango says: Here is about page!<a href='/rango'>Index</a>")

def about(request):
	context = RequestContext(request)
	context_dict = {'newbold': "It 's my about page/ :)"}
	return render_to_response('rango/new.html', context_dict, context)

def category(request, category_name_url):
	context = RequestContext(request)
	category_name = category_name_url.replace('_', ' ')
	context_dict = {'category_name': category_name}
	try:
		category = Category.objects.get(name=category_name)
		pages = Page.objects.filter(category=category)
		context_dict['pages'] = pages
		context_dict['category'] = category
	except Category.DoesNotExist:
		pass
	return render_to_response('rango/category.html', context_dict, context)
	
