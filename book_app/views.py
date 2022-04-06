from django.shortcuts import render , redirect
from django.http import HttpResponse
from book_app.models import BookList
from book_app.forms import BookForm
from django.contrib.auth.decorators import login_required

@login_required                                                     # it is the decorator which specifies that to access this view, a valid login is required
def book(request):
    
    if request.method == "POST":
        form = BookForm(request.POST or none)                       # if the request is POST method, get the data from the form and validate it
        if form.is_valid():                                         #if the form is valid, save the form in the DB and redirect to book view                   
            form.save()
        return redirect('book')
        
    else:
        all_books = BookList.objects.all()                                  #if there is not POST method, retrive all the data from DB and display
        return render(request, 'book.html', {'all_books':all_books})
    
    
@login_required    
def delete_book(request, book_id):
    book = BookList.objects.get(pk=book_id)                     #to delete a book, primary key id is must. Based on that, the book is deleted.
    book.delete()
    return redirect('book')  

@login_required
def edit_book(request, book_id):
    if request.method == "POST":                                        #to Edit the data of the book, id is required.
        book = BookList.objects.get(pk=book_id)                         #here POST method is used because we need to edit the data and save the new data in the DB.
        form = BookForm(request.POST or none, instance = book)
        if form.is_valid():
            form.save()
        return redirect('book')
        
    else:
        all_books_obj = BookList.objects.get(pk=book_id)
        return render(request, 'edit.html', {'all_books_obj':all_books_obj})


def home(request):
    
    context = {'index_text':"Welcome to Home Page",
               }
    return render(request, 'home.html',context)



def student_view(request):
                                                                        #it is the student view where in all the data related to books will be displayed 
    all_books = BookList.objects.all()                                  #without the login
    return render(request, 'student.html', {'all_books':all_books})



