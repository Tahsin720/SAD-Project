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
from django.urls import path
from E_book_library_management_system import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login_page, name='login'),
    path('signup/', views.Signup_page, name='signup'),
    path('book/',views.book_page, name='book'),
    path('signout/',views.signout_page, name='signout'),
    path('donate/',views.donate_page, name='donate'),
    path('search/',views.search_page, name='search'),
    path('Request/',views.Request_func, name='Request'),
    path('cancel Request/',views.cancel_Request_func, name='cancel Request'),
    path('likes/',views.count_likes, name='likes'),
    path('dislikes/',views.count_dislikes, name='dislikes'),
    path('my_book/',views.my_book_func, name='my_book'),
    path('my_req/',views.my_request_func, name='my_req'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
