from django.shortcuts import render

# Create your views here.
def home_view(request):
	context = {}
	template = 'home.html'

	return render(request, template, context)