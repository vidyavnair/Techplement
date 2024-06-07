
import requests
from django.shortcuts import render,redirect
from .models import Quote,CustomUser



from django.contrib import messages

def loging(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['pass']
        user = CustomUser.objects.filter(email=email, password=password).first()
        if user:
            request.session['user_id'] = user.id
            return redirect('home')
        else:
            messages.error(request, 'please register first')
    return render(request, "loging.html")

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['pass']
        password_confirm = request.POST['pass_confirm']

        if password != password_confirm:
            messages.error(request, 'Passwords do not match')
        elif CustomUser.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists')
        else:
            CustomUser.objects.create(first_name=first_name, last_name=last_name, email=email, password=password)
            messages.success(request, 'User registered successfully')
            return redirect('loging')
    return render(request, "register.html")

# for fetching random quotes from api and save it in our database Quote.


def home(request):
    quote = Quote.objects.order_by('?').first()
    return render(request, 'home.html', {'quote': quote.text, 'author': quote.author})

def search(request):
    query = request.GET.get('q')
    print(f"Searching for author: {query}")
    results = Quote.objects.filter(author__icontains=query)
    print(f"Found quotes: {query}")
    return render(request, 'search.html', {'results': results, 'query': query})
def logout(request):
    if 'user_id' in request.session:
        del request.session['user_id']
    return redirect('loging')