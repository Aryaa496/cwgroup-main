import json
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import CustomUser
from django.views.decorators.csrf import csrf_exempt

# This is the login view (Simple success message for login)
@csrf_exempt
def login_view(request):
    return JsonResponse({'message': 'Hello World!'}, status=200)

# Django authentication with email instead of username
@csrf_exempt
def login_view1(request):
    if request.method == "POST":
        # Parse JSON request body
        try:
            body = json.loads(request.body)  # Parse the JSON body
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON format.'}, status=400)

        email = body.get('email')
        password = body.get('password')

        if not email or not password:
            return JsonResponse({'error': 'Email and password are required.'}, status=400)

        # Normalize the email to handle case sensitivity
        email = email.lower()

        try:
            user = CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            return JsonResponse({'error': 'Invalid Email.'}, status=400)

        user = authenticate(request, email=email, password=password)
        if user is None:
            return JsonResponse({'error': 'Invalid Password.'}, status=400)

        login(request, user)
        return JsonResponse({'success': 'Logged in successfully.'})

    return JsonResponse({'error': 'Invalid request method.'}, status=405)

# User profile (JSON response for example)
@csrf_exempt
def user_profile(request):
    # Assuming you're fetching the logged-in user's profile from the request
    if request.user.is_authenticated:
        user_data = {
            'name': request.user.name,
            'email': request.user.email,
        }
        return JsonResponse(user_data)
    return JsonResponse({'error': 'User not authenticated'}, status=401)
