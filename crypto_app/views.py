from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Coin, UserPaymentReview
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import REDIRECT_FIELD_NAME
# Create your views here.
from .forms import UserPaymentForm

def login_required(
    function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='userauths:sign-in'
):
    """
    Decorator for views that checks that the user is logged in, redirecting
    to the log-in page if necessary.
    """
    actual_decorator = user_passes_test(
        lambda u: u.is_authenticated,
        login_url=login_url,
        redirect_field_name=redirect_field_name,
    )
    if function:
        return actual_decorator(function)
    return actual_decorator











def index(request):
    # product = Product.objects.all().order_by("-id")
    coins = Coin.objects.filter(product_status="published", featured=True)
    context = {
        "coins": coins
    }
    return render(request, "core/index.html", context)

@login_required
def coin_list_view(request):
    coins = Coin.objects.filter(product_status="published")
    context = {
        "coins": coins
    }
    return render(request, "core/product-list.html", context)

@login_required
def payment_view(request):
    return render(request, "core/wallet-details.html")

@login_required
def coin_detail_view(request, pid):
    form = UserPaymentForm()
    product = Coin.objects.get(pid=pid)
    products = Coin.objects.filter(category=product.category).exclude(pid=pid)
    p_image = product.product_image()
    
    if request.method == 'POST':
        form = UserPaymentForm(request.POST or None)
        if form.is_valid():
            # Save the order to the database
            form.save()
            # Redirect to a confirmation page or another relevant page
            return redirect('core:payment')
    else:
        
        form = UserPaymentForm()
    context = {
        "form": form,
        "p": product,
        "p_image": p_image,
        "products": products,
        
    }
    
    return render(request, "core/product-detail.html", context)

@login_required
def dashboard_view(request):
    coins = Coin.objects.filter(product_status="published")

    context = {
        "coins": coins
    }
    return render(request, "core/dashboard-crypto.html", context)

@login_required
def profile_view(request):
    return render(request, "core/pages-profile.html")

@login_required
def profile_settings_view(request):

    return render(request, "core/pages-profile-settings.html")






