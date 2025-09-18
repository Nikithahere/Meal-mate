from django.shortcuts import render
from django.http import HttpResponse
from .models import Customer

# Home page
def index(request):
    return render(request, 'index.html')

# Open signin page
def open_signin(request):
    return render(request, 'signin.html')

# Open signup page
def open_signup(request):
    return render(request, 'signup.html')

# Signup new customer
def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        address = request.POST.get('address')

        # Prevent anyone from registering as admin
        if username.lower() == "admin":
            return HttpResponse("Username 'admin' is reserved!")

        try:
            Customer.objects.get(username=username)
            return HttpResponse("Duplicate usernames are not allowed...")
        except Customer.DoesNotExist:
            # Create new customer
            Customer.objects.create(
                username=username,
                password=password,
                email=email,
                mobile=mobile,
                address=address
            )
            return render(request, "signin.html")

# Signin function
def signin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # ✅ Special case for admin
        if username == "admin" and password == "admin":   # set your own admin password here
            return render(request, 'admin_home.html')

        try:
            Customer.objects.get(username=username, password=password)
            return render(request, "customer_home.html")
        except Customer.DoesNotExist:
            return render(request, 'fail.html')

    # If user just opens /signin/ directly
    return render(request, 'signin.html')

# Admin: Add restaurant page
def add_restaurant_page(request):
    return render(request, "add_restaurant.html")