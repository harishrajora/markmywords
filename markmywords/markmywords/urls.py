"""markmywords URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from home import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name = "index"),
    path('loginpage', views.loginpage, name = "loginpage"),
    path('loginuser', views.loginuser, name = "loginuser"),
    path('logoutuser', views.logoutuser, name = "logoutuser"),
    path('dashboard', views.dashboard, name = "dashboard"),
    path('signup', views.signup, name = "signup"),
    path('search_word', views.search_word, name = "search_word"),
    path('search_word_page', views.search_word_page, name = "search_word_page"),
    path('save_the_word', views.save_the_word, name = "save_the_word")
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
