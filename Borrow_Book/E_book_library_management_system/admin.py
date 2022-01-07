from django.contrib import admin
from . models import my_request, book, my_request_log, Review_for_books, book_log, Profile, Report, payment

# Register your models here.
admin.site.register(my_request)
admin.site.register(book)
admin.site.register(book_log)
admin.site.register(my_request_log)
admin.site.register(Review_for_books)
admin.site.register(Profile)
admin.site.register(Report)
admin.site.register(payment)