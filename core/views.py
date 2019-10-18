from django.shortcuts import render

# Create your views here.
def home_view(request):
	context = {}
	template = 'home.html'

	return render(request, template, context)


def home_mvp_view(request):

	context = {}
	template = 'home-mvp.html'

	return render(request, template, context)