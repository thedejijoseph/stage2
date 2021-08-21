
import random

from django.shortcuts import render, redirect

from .models import Contact
# Create your views here.

def index(request):
    return render(request, 'landing/index.html')
    
def contact(request):
    if request.method == "GET":
        return redirect('index')
    elif request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        contact = Contact(name=name, email=email, message=message)
        contact.save()

        reactions = ["😉", "😎", "😄", "🤖", "✌️"]
        reaction = random.choice(reactions)

        return render(request, 'landing/thanks.html', {'name': name, "reaction": reaction})
