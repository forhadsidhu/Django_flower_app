"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url, include
from myapp import views as myapp_views
from rest_framework.schemas import get_schema_view

from django.conf import settings
from django.conf.urls.static import static
schema_view = get_schema_view(title='Flower API')
urlpatterns = [
    path('admin/', admin.site.urls),
    # You can use angle brackets to capture values from the URL
    path('flower/create/', myapp_views.create, name='create'),
    path('flower/delete/<int:pk>/', myapp_views.delete, name='delete'),
    path('flower/<slug:slug>/', myapp_views.detail, name='detail'),
    path('tags/<slug:slug>/', myapp_views.tags, name='tags'),
    path('', myapp_views.index, name='index'),
    path('accounts/',include('allauth.urls')),
    path('schema/',schema_view)



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # using static() helper function
# In the development phase you can server these user-uploaded files using static() helper function
#Heroku platform we will serve the media
# files from an Amazons AWS bucket
#You can use static() function to serve the files in debug mode