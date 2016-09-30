from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from .models import Book
from django.db import connection
# Create your views here.
def index(request) :
    return render(request,'bookstore/index.html')

def listbook(request) :
    book = ""
    for row in Book.objects.raw('SELECT * FROM bookstore_book'):
         book += '''
                <tr>
                    <td>'''+str(row.book_id)+'''</td>
                    <td>'''+str(row.ISBN)+'''</td>
                    <td>'''+str(row.book_name)+'''</td>
                    <td>'''+str(row.price)+'''</td>
                    <td>'''+str(row.author)+'''</td>
                    <td><a href="update/?id='''+str(row.book_id)+'''">Update</a></td>
                    <td><a href="delete/?id='''+str(row.book_id)+'''">Delete</a></td>
                </tr>
                '''
    message = """<html>
                    <head></head>
                    <body>
                        <table border="1">
                            """+book+"""
                        </table>
                    </body>
                  </html>"""

    return HttpResponse(message)

def insertbook(request) :
    ISBN = request.POST['ISBN']
    book_name = request.POST['book_name']
    price = request.POST['price']
    author = request.POST['author']
    book_id = request.POST['book_id']
    book = Book.objects.create(ISBN=ISBN,book_name=book_name,price=price,author=author,book_id=book_id)
    book.save()
    return HttpResponseRedirect(reverse('bookstore:listbook'))

def update(request):
    book_id = request.GET.get('id','')

    with connection.cursor() as curser:
        cursor.execute("UPDATE bookstore_book SET ISBN='1234', book_name='P3xx', price=100, author='a' where book_id= %d", book_id)
        cursor.execute("SELECT * FROM bookstore_book where book_id= %d", book_id)
        row = cursor.fetchone()

    return HttpResponse(row)

def delete(request) :
    book_id = request.GET.get('id','')
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM bookstore_book where book_id= %s", book_id)
        cursor.execute("SELECT * FROM bookstore_book")
        row = cursor.fetchone()

    return HttpResponse(row)
