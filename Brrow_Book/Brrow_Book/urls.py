"""Brrow_Book URL Configuration

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
from django.urls import path, include
from E_book_library_management_system import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('login/', views.login_page, name='login'),
    # path('signup/', views.Signup_page, name='signup'),
    # path('home/',views.home_page, name='home'),
    # path('signout/',views.signout_page, name='signout'),
    # path('donate/',views.donate_page, name='donate'),
    # path('', include("django.contrib.auth.urls")),
    # path('search/',views.search_page, name='search'),
    # path('likes/',views.count_dislikes, name='likes'),
    # path('dislikes/',views.count_likes, name='dislikes'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
