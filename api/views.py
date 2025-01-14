from django.http import HttpResponse, HttpRequest, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import CustomUser 
from django.views.decorators.csrf import csrf_exempt

 # Import your custom user model

# Main SPA (Single Page Application) view
def main_spa(request: HttpRequest) -> HttpResponse:
    return render(request, 'api/spa/index.html', {})

# This is the login view
def login_view(request):
    return HttpResponse("Hello world!")

# Django authentication with email instead of username
@csrf_exempt
def login_view1(request):
    if request.method == "POST":
        email = request.POST.get('email')  # Get email input from form
        password = request.POST.get('password')
        
        # Check if a user with the provided email exists
        try:
            user = CustomUser.objects.get(email=email)  # Use CustomUser model
        except CustomUser.DoesNotExist:
            messages.error(request, 'Invalid Email')
            return redirect('/login/')
        
        # Authenticate the user with the provided email and password
        user = authenticate(request, email=email, password=password)
        
        if user is None:
            messages.error(request, "Invalid Password")
            return redirect('/login/')
        else:
            # Log in the user and redirect to the home page upon successful login
            login(request, user)
            return redirect('/home/')
    
    # Render the login page template (GET request)
    return render(request, 'login.html')
@csrf_exempt
def user_profile(request):
    
    user_data={
        'name':request.POST.get('name'),
        'email':request.POST.get('email'),
        

    }
    return JsonResponse(user_data)
