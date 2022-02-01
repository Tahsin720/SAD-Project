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
from django.contrib.auth.decorators import login_required
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_page, name='home'),
    path('login/', views.login_page, name='login'),
    path('signup/', views.Signup_page, name='signup'),
    path('profile/', views.profile_page, name='profile'),
    path('profile_func/', views.profile_func, name='profile_func'),
    path('signout/',views.signout_page, name='signout'),

    path('search/',views.search_page, name='search'),
    
    path('book/',views.book_page, name='book'),
    path('donate/',views.donate_page, name='donate'),
    path('Request/',views.Request_func, name='Request'),
    path('likes/',views.count_likes, name='likes'),
    path('dislikes/',views.count_dislikes, name='dislikes'),
    
    path('my_req/',views.my_request_func, name='my_req'),
    path('cancel Request/',views.cancel_Request_func, name='cancel Request'),
    
    path('my_book/',views.my_book_func, name='my_book'),
    path('Delete_book/',views.Delete_book_func, name='Delete_book'),
    path('edit_book/',views.edit_book_page, name='edit_book'),
    path('update_book/',views.update_book_func, name='update_book'),

    path('Post/',views.Post, name='Post'),
    path('Edit/',views.edit_review_page, name='Edit'),
    path('update_edit/',views.update_rev_func, name='update_edit'),
    path('Review/',views.Review_page, name='Review'),
    path('del_Review/',views.del_Review_func, name='del_Review'),

    path('payment/',views.payment_page, name='payment'),
    path('payment_func/',views.payment_func, name='payment_func'),
    path('choose_plan/',views.choose_plan, name='choose_plan'),
    
    path('report/',views.report_function, name='report'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns += staticfiles_urlpatterns()

