from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from . models import my_request, book
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def admin_login(request):
    return render(request, '/admin')

def login_page(request):
    if request.method == 'POST':
        username = request.POST['user']
        password = request.POST['password']

        print(username, password)
        user = authenticate(username=username, password=password)

        if user is None:
            print('Not Done')
            messages.error(request, 'Failed!')
            return redirect('login')
        else:
            login(request, user)
            print('Done')
            messages.success(request, 'Logged In!')
            
            return redirect('book')
    else:
        messages.error(request, 'Failed!')
        return render(request,'E_book_library_management_system/login.html')
    


def signout_page(request):
    logout(request)
    return redirect('login')

def Signup_page(request):
    if request.method == 'POST':
        username = request.POST['user']
        password = request.POST['password']
        email = request.POST['email']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']

        Us = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
        Us.save()

        print('User Created!')
        return redirect('login')
    else:
        return render(request, 'E_book_library_management_system/signup.html')

def donate_page(request):
    if request.method == 'POST':
        isbn = request.POST['isbn']
        name = request.POST['name']
        author = request.POST['author']
        des = request.POST['description']
        user_name = request.POST['user']
        isdonate = request.POST['IsDonated']
        if len(request.FILES) != 0:
            image = request.FILES['photo']

        Book = book(isbn=isbn, name=name, author=author, user_name=user_name, description=des, isdonated=isdonate, image=image)
        Book.save()
        print('Donated!')
        return redirect('book')
    else:
        return render(request, 'E_book_library_management_system/donate.html')

def book_page(request):
    b_page = book.objects.all()
    return render(request, 'E_book_library_management_system/book.html', {'book_page': b_page})

def search_page(request):
    if request.method == 'POST':
        name = request.POST['search']
        b = book.objects.filter(name = name)
        return render(request, 'E_book_library_management_system/search.html', {'book': b})
    else:
        return redirect('book')

def Request_func(request):
    if request.method == 'GET':
        id = request.GET['isbn']
        name = request.GET['uname']
        if not my_request.objects.filter(isbn = id, requester = name).exists():
            r = my_request(isbn = id, requester = name)
            r.save()
            return redirect('book')
        else:
            messages.error(request, 'Data already exists!')
            return redirect('book')
    else:
        messages.error(request, 'Failed!')
        return redirect('book')

def cancel_Request_func(request):
        if request.method == 'GET':
            id = request.GET['isbn']
            if my_request.objects.filter(isbn = id).exists():
                r = my_request.objects.get(isbn = id)
                r.delete()
                return redirect('book')
            else:
                messages.error(request, 'No Such Data')
                return redirect('book')
        else:
            messages.error(request, 'failed')
            return redirect('book')

def count_likes(request):
        if request.method == 'GET':
            id = request.GET['isbn']
            if book.objects.filter(isbn = id).exists():
                r = book.objects.get(isbn = id)
                r.likes += 1
                r.save()
                return redirect('book')
            else:
                messages.error(request, 'No Such Data')
                return redirect('book')
        else:
            messages.error(request, 'failed')
            return redirect('book')

def count_dislikes(request):
        if request.method == 'GET':
            id = request.GET['isbn']
            if book.objects.filter(isbn = id).exists():
                r = book.objects.get(isbn = id)
                r.dislikes += 1
                r.save()
                return redirect('book')
            else:
                messages.error(request, 'No Such Data')
                return redirect('book')
        else:
            messages.error(request, 'failed')
            return redirect('book')

def my_book_func(request):
    if book.objects.filter(user_name = request.user.username).exists(): 
        b_page = book.objects.filter(user_name = request.user.username)
        return render(request, 'E_book_library_management_system/my_book.html', {'book_page': b_page})
    else:
        return render(request, 'E_book_library_management_system/my_book.html')