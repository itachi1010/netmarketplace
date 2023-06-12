from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView




urlpatterns = [
    path('core/', include('core.urls')),
    path('items/', include('item.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('inbox/', include('conversation.urls')),
    path('admin/', admin.site.urls),
    path("accounts/", include("accounts.urls")),  # new
    path('accounts/', include("django.contrib.auth.urls")),
    
]


'''
these are for netlodge 
urlpatterns = [
    path('core/', include('core.urls')),
    path('admin/', admin.site.urls),
    path('', include('landing_page.urls', namespace='landing_page')),
    path("accounts/", include("accounts.urls")),  # new
    path('accounts/', include("django.contrib.auth.urls")),
    path('items/', include('item.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('inbox/', include('conversation.urls')),
    #path('', TemplateView.as_view(template_name='index.html'), name='index'),
]
'''
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)




