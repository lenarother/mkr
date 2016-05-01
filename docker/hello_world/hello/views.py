from django.shortcuts import render
from models import Quotes

def hello(request):
    return render(request, 'hello/hello.html', {})

def quote(request):
    """Requests a quote from the database and displays it."""
    quote = Quotes.objects.first()
    return render(request, 'hello/quote.html', {"quote": str(quote) })
