from django.shortcuts import render
from .forms import SignupForm
from django.core.mail import EmailMultiAlternatives
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.urls import reverse






#i added this 
def signup(request):
    form = SignupForm()
    
    return render(request, 'landing_page/signup.html',{
        'form':form
    })


# Initial landing page view.
def index(request):
    return render(request, 'landing_page/index.html')

def aboutus(request):
    return render(request, 'landing_page/aboutus.html')

def blog(request):
    return render(request, 'landing_page/blog-post-list.html')
def contactus(request):
    return render(request, 'landing_page/contact-us.html')
def features(request):
    return render(request, 'landing_page/features.html')
def login(request):
    return render(request, 'landing_page/login.html')
def payment(request):
    return render(request, 'landing_page/payment-page.html')
def pricing(request):
    return render(request, 'landing_page/pricing.html')
def product(request):
    return render(request, 'landing_page/product-page.html')
def registration(request):
    return render(request, 'landing_page/registration.html')
def service(request):
    return render(request, 'landing_page/service-page.html')
def shoppingcart(request):
    return render(request, 'landing_page/shopping-cart.html')


#Add other views here