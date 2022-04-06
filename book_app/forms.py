from django import forms

from book_app.models import BookList

class BookForm(forms.ModelForm):
    class Meta:
        model = BookList                                                            #to use django forms to get the input from the user and store it in the DB
        fields = ['name','author','studentno' ,'studentname', 'issuedate']
    