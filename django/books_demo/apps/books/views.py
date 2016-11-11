from django.shortcuts import render, redirect
from .models import Author, Book

# Create your views here.
def index(request):
	stephen_king = Author.objects.get(name="Stephen King")
	context = {
		"authors": Author.objects.all(),
		"books": stephen_king.books.exclude(rating__lte=5),
	}
	return render(request, "books/index.html", context)

def create_author(request):
	new_author = Author()
	new_author.name = request.POST["name"]
	new_author.save()

	return redirect("index")

def create_book(request):
	author = Author.objects.get(id=request.POST["author"])
	Book.objects.create(title=request.POST["title"], rating=request.POST["rating"], author=author)
	return redirect("index")