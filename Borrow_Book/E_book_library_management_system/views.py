 
    
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from . models import my_request, book, my_request_log, Review_for_books, book_log, Report, Profile, payment 
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from datetime import datetime



def admin_login(request):
    return render(request, '/admin')


def home_page(request):
    return render(request, 'E_book_library_management_system/home.html')


def login_page(request):
    if request.method == 'POST':
        username = request.POST['user']
        password = request.POST['password']

        print(username, password)
        user = authenticate(username=username, password=password)

        if user is None:
            print('Not Done')
            messages.error(request, 'Invalid Username or Password')
            return redirect('login')
        else:
            login(request, user)
            print('Done')
            messages.success(request, 'Logged In!')
            
            return redirect('home')
    else:
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
      

@login_required   
def profile_page(request): 
    if Profile.objects.filter(user = request.user.id).exists(): 
        p_page = Profile.objects.filter(user = request.user.id)
        return render(request, 'E_book_library_management_system/profile.html', {'profile_page': p_page})
    else:
        return render(request, 'E_book_library_management_system/book.html')

   
@login_required        
def profile_func(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        mobile_num = request.POST['mobile']
        location = request.POST['location']
        password = request.POST['password']
        new_password = request.POST['new_password']
        re_password = request.POST['re_password']
        if mobile_num != "None" and location != "None":
            if len(request.FILES) != 0:
                image = request.FILES['photo']
                if password == "":
                    if Profile.objects.filter(user = request.user.id).exists():
                        u = Profile.objects.get(user=request.user.id)
                        u.image = image
                        u.save()
                        Profile.objects.filter(user = request.user.id).update(mobile_num = mobile_num, location = location) 
                        User.objects.filter(id = request.user.id).update(first_name = first_name, last_name = last_name, email = email)
                        return redirect('profile')
                else:
                    if Profile.objects.filter(user = request.user.id).exists():
                        if User.objects.filter(id = request.user.id).exists():
                            user = User.objects.get(id = request.user.id)
                            check = user.check_password(password)
                            if new_password != "" and re_password != "":
                                if new_password == re_password:
                                    if check == True:
                                        u = Profile.objects.get(user=request.user.id)
                                        u.image = image
                                        u.save()
                                        Profile.objects.filter(user = request.user.id).update(mobile_num = mobile_num, location = location) 
                                        User.objects.filter(id = request.user.id).update(first_name = first_name, last_name = last_name, email = email)
                                        user.set_password(new_password)
                                        user.save()
                                        User.objects.filter(id = request.user.id).update(first_name = first_name, last_name = last_name, email = email)
                                        logout(request)
                                        return redirect('login')
                                else:
                                    messages.error(request, 'Did not match password!')
                                    return redirect('profile')
                            else:
                                if Profile.objects.filter(user = request.user.id).exists():
                                    Profile.objects.filter(user = request.user.id).update(mobile_num = mobile_num, location = location) 
                                    User.objects.filter(id = request.user.id).update(first_name = first_name, last_name = last_name, email = email)
                                    return redirect('profile')
                        else:
                            return redirect('profile')
            else:
                if password == "":
                    if Profile.objects.filter(user = request.user.id).exists():
                        Profile.objects.filter(user = request.user.id).update(mobile_num = mobile_num, location = location) 
                        User.objects.filter(id = request.user.id).update(first_name = first_name, last_name = last_name, email = email)
                        return redirect('profile')
                else:
                    if Profile.objects.filter(user = request.user.id).exists():
                        if User.objects.filter(id = request.user.id).exists():
                            user = User.objects.get(id = request.user.id)
                            check = user.check_password(password)
                            if new_password != "" and re_password != "":
                                if new_password == re_password:
                                    if check == True:
                                        user.set_password(new_password)
                                        user.save()
                                        User.objects.filter(id = request.user.id).update(first_name = first_name, last_name = last_name, email = email)
                                        logout(request)
                                        return redirect('login')
                                else:
                                    messages.error(request, 'Did not match password!')
                                    return redirect('profile')
                            else:
                                if Profile.objects.filter(user = request.user.id).exists():
                                    Profile.objects.filter(user = request.user.id).update(mobile_num = mobile_num, location = location) 
                                    User.objects.filter(id = request.user.id).update(username = username, first_name = first_name, last_name = last_name, email = email)
                                    return redirect('profile')
                        else:
                            print("Foooooouuuuunnnnnddddd")
                            return redirect('profile')
        else:
            messages.error(request, 'Fill the Mobile number and Location field!') 
            return redirect('profile')
    else:
        return render(request, 'E_book_library_management_system/profile.html')

@login_required   
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

        Book = book(isbn=isbn, name=name, author=author, user_name=user_name, description=des, isdonated=isdonate, image=image, time=datetime.now())
        Book.save()
        Book_log = book_log(isbn=isbn, name=name, author=author, user_name=user_name, date_time=datetime.now())
        Book_log.save()
        print('Donated!')
        return redirect('book')
    else:
        return render(request, 'E_book_library_management_system/donate.html')


@login_required   
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
    
@login_required   
def Request_func(request):
    if request.method == 'GET':
        id = request.GET['isbn']
        print("isbn: ", id)
        name = request.GET['uname']
        print("name: ", name)
        book_name = request.GET['book_name']
        print("book_name: ", book_name)

        if not my_request.objects.filter(isbn = id, requester = name).exists():
            r = my_request(isbn = id, requester = name, time = datetime.now())
            r.save()
            print("Req=> Save", )
            request_log = my_request_log(isbn = id, requester = name, name = book_name, date_time = datetime.now())
            request_log.save()
            return redirect('book')
        else:
            request_log = my_request_log(isbn = id, requester = name, name = book_name, date_time = datetime.now())
            request_log.save()
            messages.error(request, 'Data already exists!')
            return redirect('book')
    else:
        messages.error(request, 'Failed!')
        return redirect('book')

@login_required   
def cancel_Request_func(request):
        if request.method == 'GET':
            id = request.GET['isbn']
            if my_request.objects.filter(isbn = id).exists():
                r = my_request.objects.filter(isbn = id)
                r.delete()
                return redirect('book')
            else:
                messages.error(request, 'No Such Data')
                return redirect('book')
        else:
            messages.error(request, 'failed')
            return redirect('book')

@login_required   
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
@login_required   
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
        
        
@login_required   
def my_book_func(request):
    if book.objects.filter(user_name = request.user.username).exists(): 
        b_page = book.objects.filter(user_name = request.user.username)
        return render(request, 'E_book_library_management_system/my_book.html', {'book_page': b_page})
    else:
        return render(request, 'E_book_library_management_system/my_book.html')
    
    
@login_required   
def my_request_func(request):
    #print("Okkkkakkaaakakkakakakak")
    if my_request.objects.filter(requester = request.user.username).exists(): 
        print("Okkkkakkaaakakkakakakak")
        r_page = my_request.objects.filter(requester = request.user.username)
        
        return render(request, 'E_book_library_management_system/my_req.html', {'req_page': r_page})
    else:
        return render(request, 'E_book_library_management_system/my_req.html')
    
    
@login_required   
def Post(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        name = request.POST['book_name']
        author = request.POST['book_author']
        text = request.POST['post']
        Rev = Review_for_books(posted_by=uname, name=name, author=author, text=text, date_time = datetime.now())
        Rev.save()
        print('Posted!')
        return redirect('Review')
    else:
        return render(request, 'E_book_library_management_system/post.html')


@login_required   
def Review_page(request):
    r_page = Review_for_books.objects.all()
    u_page = User.objects.all()
    return render(request, 'E_book_library_management_system/Review.html', {'rev_page': r_page, 'user_page': u_page})


@login_required   
def del_Review_func(request):
    if request.method == 'GET':
        Id = request.GET['Id']
        if Review_for_books.objects.filter(Id = Id).exists():
            rev = Review_for_books.objects.filter(Id = Id)
            rev.delete()
            return redirect('Review')
        else:
            messages.error(request, 'No Such Data')
            return redirect('Review')
        
    else:
        messages.error(request, 'failed')
        return redirect('Review')


@login_required   
def edit_review_page(request):
    if request.method == 'GET':
        Id = request.GET['Id']
        if Review_for_books.objects.filter(Id = Id).exists():
            r_page = Review_for_books.objects.filter(Id = Id)
            return render(request, 'E_book_library_management_system/edit.html', {'rev_page': r_page})
    else:
        messages.error(request, 'failed')
        return redirect('Review')


@login_required   
def update_rev_func(request):
    if request.method == 'POST':
        Id = request.POST['Id']
        uname = request.POST['uname']
        name = request.POST['book_name']
        author = request.POST['book_author']
        text = request.POST['post']
        if Review_for_books.objects.filter(Id = Id).exists():
            Review_for_books.objects.filter(Id = Id).update(posted_by=uname, name=name, author=author, text=text)
            print('Posted!')
            return redirect('Review')
    else:
        return render(request, 'E_book_library_management_system/post.html')


@login_required   
def Delete_book_func(request):
    if request.method == 'GET':
            id = request.GET['isbn']
            if book.objects.filter(isbn = id).exists():
                r = book.objects.filter(isbn = id)
                r.delete()
                return redirect('my_book')
            else:
                messages.error(request, 'No Such Data')
                return redirect('book')
    else:
        messages.error(request, 'failed')
        return redirect('book')


@login_required   
def edit_book_page(request):
    if request.method == 'GET':
        Id = request.GET['isbn']
        if book.objects.filter(isbn = Id).exists():
            b_page = book.objects.filter(isbn = Id)
            return render(request, 'E_book_library_management_system/update_book.html', {'book_page': b_page})
    else:
        messages.error(request, 'failed')
        return redirect('my_book')


@login_required   
def update_book_func(request):
    if request.method == 'POST':
        isbn = request.POST['isbn']
        print("ISBN======>", isbn)
        name = request.POST['name']
        author = request.POST['author']
        des = request.POST['description']
        isdonate = request.POST['IsDonated']
        if book.objects.filter(isbn = isbn).exists():
            if len(request.FILES) != 0:
                image = request.FILES['photo']
                u = book.objects.get(isbn=isbn)
                u.image = image
                u.save()
                book.objects.filter(isbn = isbn).update(name=name, author=author, description=des, isdonated=isdonate, time=datetime.now())
            else:
                book.objects.filter(isbn = isbn).update(name=name, author=author, description=des, isdonated=isdonate, time=datetime.now())    

        print('Donated!')
        return redirect('my_book')
    else:
        return render(request, 'E_book_library_management_system/update_book.html')


@login_required   
def report_function(request):
    if request.method == 'GET':
        Id = request.GET['Id']
        reporter = request.GET['user_name']
        if not Report.objects.filter(id = Id).exists():
            if Review_for_books.objects.filter(Id = Id).exists():
                rev = Review_for_books.objects.get(Id = Id)
                re = Report(id = rev.Id, posted_by = rev.posted_by, name = rev.name, author = rev.author, text = rev.text, reporter = reporter, date_time = datetime.now())
                re.save()
                return redirect('Review')
            else:
                messages.error(request, 'No such data')
                return redirect('Review')
        else:
            messages.error(request, 'Already Inserted')
            return redirect('Review')


@login_required   
def payment_page(request):
    if request.method == 'GET':
        amount = request.GET['amount']
        return render(request, 'E_book_library_management_system/payment.html', {'amount': amount})
    else:
        print("<=====Else=====>: ")
        return render(request, 'E_book_library_management_system/choose_plan.html')


@login_required   
def choose_plan(request):
    return render(request, 'E_book_library_management_system/choose_plan.html')


@login_required   
def payment_func(request):
    if request.method == 'POST':
        paid_by = request.POST['paid_by']
        account_num = request.POST['acc_no']
        amount = request.POST['amount']
        payment_method = request.POST['payment-method']
        pay = payment(paid_by = paid_by, account_num = account_num, amount = amount, payment_method = payment_method, date_time = datetime.now())
        pay.save()
        if amount == "100":
            p = Profile.objects.get(user = request.user.id)
            Profile.objects.filter(user = request.user.id).update(balance = 105 + p.balance)
            return redirect('profile')
        elif amount == "1000":
            p = Profile.objects.get(user = request.user.id)
            Profile.objects.filter(user = request.user.id).update(balance = 1200 + p.balance)
            return redirect('profile')
        elif amount == "500":
            p = Profile.objects.get(user = request.user.id)
            Profile.objects.filter(user = request.user.id).update(balance = 650 + p.balance)
            return redirect('profile')
        elif amount == "2000":
            p = Profile.objects.get(user = request.user.id)
            Profile.objects.filter(user = request.user.id).update(balance = 3000 + p.balance)
            return redirect('profile')

    return render(request, 'E_book_library_management_system/choose_plan.html')