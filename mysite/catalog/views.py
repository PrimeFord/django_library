from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Book, Author, BookInstance, Genre

# Create your views here.
# def catalog(request):
#     return HttpResponse("Hello world!")

# Using template for Html views
# def catalog(request):
#   template = loader.get_template('index.html')
#   return HttpResponse(template.render())

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)