from django.shortcuts import render,redirect
from .models import Product
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required



def home(request):
    # if no one is "logged in", send back to login
    if "user" not in request.session:
        return redirect("login")
    return render(request, "home.html", {"user": request.session["user"]})

def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        # ✅ Ignore real authentication, just allow anyone
        request.session["user"] = email  # save in session
        return redirect("home")

    return render(request, "login.html")


def logout_view(request):
    request.session.flush()  # clear session
    return redirect("login")




def shop(request):
    # Product list
    products = [
        {"name": "Eraser", "price": 10, "category": "eraser", "image": 'images/20.jpg'},
        {"name": "keychain", "price": 5, "category": "others", "image": 'images/21.jpg'},
        {"name": "pens", "price": 3, "category": "pen", "image": 'images/22.jpg'},
        {"name": "set", "price": 3, "category": "others", "image": 'images/23.jpg'},
        {"name": "other", "price": 3, "category": "others", "image": 'images/24.jpg'},
        {"name": "other", "price": 3, "category": "others", "image": 'images/25.jpg'},
        {"name": "mini book", "price": 3, "category": "book", "image": 'images/26.jpg'},
        {"name": "sticky notes", "price": 3, "category": "others", "image": 'images/28.jpg'},
        {"name": "sticky notes", "price": 3, "category": "others", "image": 'images/29.jpg'},
        {"name": "keychain", "price": 3, "category": "others", "image": 'images/30.jpg'},
        {"name": "Bread eraser", "price": 3, "category": "others", "image": 'images/21.jpg'},
        {"name": "pen", "price": 3, "category": "pen", "image": 'images/pen.jpg'},
        {"name": "pen", "price": 3, "category": "pen", "image": 'images/pen1.jpg'},
        {"name": "pen", "price": 3, "category": "pen", "image": 'images/pen3.jpg'},
        {"name": "pen", "price": 3, "category": "pen", "image": 'images/pen4.jpg'},
        {"name": "pen", "price": 3, "category": "pen", "image": 'images/pen5.jpg'},
    ]

    # Get filters from request
    query = request.GET.get('search', '').strip().lower()
    category_filter = request.GET.get('category', '').strip().lower()

    # Filter by search text
    if query:
        products = [
            p for p in products
            if query in p["name"].lower() or query in p["category"].lower()
        ]

    # Filter by category
    if category_filter:
        products = [
            p for p in products
            if p["category"].lower() == category_filter
        ]

    return render(request, 'shop.html', {
        'products': products
    })

def cart(request):
    return render(request, 'cart.html')
