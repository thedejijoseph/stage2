from django.shortcuts import render, redirect

from .models import Contact
# Create your views here.

def index(request):
    return render(request, 'landing/index.html')
    
def contact(request):
    if request.method == "GET":
        return redirect('index')
    elif request.method == "POST":
        name = request.POST.get('name', 'mate')
        email = request.POST.get('email', 'you@mates.com')
        message = request.POST.get('message', 'Hello, mate')

        contact = Contact(name=name, email=email, message=message)
        contact.save()

        return render(request, 'landing/thanks.html', {'name': name})
