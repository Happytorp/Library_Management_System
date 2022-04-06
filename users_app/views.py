from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.

def register(request):
    
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']                            #collecting the user details from register html page
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']
        
        if password==password1:
            if User.objects.filter(email=email).exists():                                                  #using the User Model
                messages.info(request,"Email already exist, Please try with another email")
                return redirect('register')                                                         #checking if email and username already exist or not and printing the error messages
            elif User.objects.filter(username=username).exists(): 
                messages.info(request,"Username already taken")
                return redirect('register')
            else:    
                user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)   #storing the details for the user in DB
                user.save()
                messages.info(request,"User registered Successfully. Login to Continue")
                return redirect('login')
        else:
            messages.info(request,"Password not matching")
        return redirect('register')
    else:
        return render(request, 'register.html',{})



def login(request):
    if request.method =="POST":
        username = request.POST['username']                                 #getting the username and password from login html page
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)                #authenticating the user using auth model
        
        if user is not None:
            auth.login(request,user)                                              #if proper user, logging in 
            return redirect('book')
        else:
            messages.info(request,"Invalid Credentials")                        # if the user is not present, displaying the error messsage
            return redirect('login')
    else:
        return render(request, 'login.html',{})
    
    
    
    
def logout(request):
    auth.logout(request)                                                        # logging out the user and redirecting it to home page
    messages.info(request,"Logged Out Successfully")
    return redirect("home")