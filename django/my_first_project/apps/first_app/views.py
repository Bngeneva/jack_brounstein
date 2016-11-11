from django.shortcuts import render

def index(request):
	context = {
		"name": "Jack",
		"food": "banana"
	}
	return render(request, "first_app/index.html", context)
