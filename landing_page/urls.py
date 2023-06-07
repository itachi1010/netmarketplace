from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


app_name = 'landing_page'

urlpatterns = [
    path('', views.index, name='index'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('signup/', views.signup, name='signup'),
    path('blog/', views.blog, name='blog'),
    path('contactus/', views.contactus, name='contactus'),
    path('features/', views.features, name='features'),
    path('login/', views.login, name='login'),
    path('payment/', views.payment, name='payment'),
    path('pricing/', views.pricing, name='pricing'),
    path('product/', views.product, name='product'),
    path('registration/', views.registration, name='registration'),
    path('service/', views.service, name='service'),
    path('shoppingcart/', views.shoppingcart, name='shoppingcart')
]