from django.shortcuts import render

def hello(request):
    return render(request, 'hello/hello.html', {})

def quote(request):
    """Requests a quote from the database and displays it."""
    quote = "bla blablabla bla bla, bla blabla bla (B. Bla)"
    return render(request, 'hello/quote.html', {"quote": quote})
