from django.db import models

class BookList(models.Model):
    
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)                                #creating the book fields for record purpose.
    studentno = models.CharField(max_length=50, default="")
    studentname = models.CharField(max_length=50,default="")
    issuedate = models.CharField(max_length=50,default="")
    
    def __str__(self):
        return self.name + " "+ self.author + " "+ self.studentno+ " "+ self.studentname+ " "+ self.issuedate   #to display the content in the admin page
    
