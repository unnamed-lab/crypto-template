from django.shortcuts import render,redirect
from userauths.forms import UserRegisterForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.conf import settings
from .decorators import restrict_view_on_wallet_create
from django.contrib.auth import logout
from userauths.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
# from django.utils.encoding import force_bytes, force_str, force_text, DjangoUnicodeDecodeError
from .utils import generate_token
from django.core.mail import EmailMessage
from django.conf import settings
import threading

# class EmailThread(threading.Thread):
#     def __init__(self, email):
#         self.email = email
#         threading.Thread.__init__(self)

#     def run(self):
#         self.email.send()



# def send_activation_email(user,request):
#     current_site = get_current_site(request)
#     email_subject = "Activate  your account"
#     context = {
#         'user': user,
#         'domain': current_site,
#         'uid': urlsafe_base64_encode(force_bytes(user.pk)),
#         'token': generate_token.make_token(user)
#     }
#     email_body = render_to_string('userauths/activate.html', context)

#     email = EmailMessage(subject=email_subject, body=email_body, from_email=settings.EMAIL_FROM_USER, to=[user.email])
#     EmailThread(email).start()



# User = settings.AUTH_USER_MODEL

def register_view(request):

    form = UserRegisterForm()
    if request.method == "POST":
        address = request.POST['address']
        username = request.POST['username']
        form = UserRegisterForm(request.POST or None)
        
        if form.is_valid():
            
            new_user = form.save()
            
            username = form.cleaned_data.get("username")
            messages.success(request, f"Hey {username}, account created successfully")
            new_user = authenticate(username=form.cleaned_data['email'],
                                    password=form.cleaned_data['password1']
            )
            # send_activation_email(new_user,request)
            login(request, new_user)
            return redirect("core:dashboard")
    context = {
        'form': form,
    }
    return render(request, 'userauths/sign-up.html', context)

def login_view(request):
    if request.user.is_authenticated:
        return redirect("core:index")
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
            user = authenticate(request, email=email, password=password)
            # if user.is_email_verified:
            #     messages.warning(request, "Email is not verified, please check your email inbox.")
            #     return render(request, "core/dashboard-crypto.html")
            if user is not None:
                login(request, user)
                messages.success(request, "Successfully logged in.")
                return redirect("core:dashboard")
            else:
                messages.warning(request, "User Doesn't Exist, create an account.")
        except:
            messages.warning(request, f"User does not exist")


    return render(request, 'userauths/sign-in.html' )

def logout_view(request):
    logout(request)
    # messages.success(request, "User successfully logged out.")
    return redirect("core:index")

def lock_screen_view(request):
    logout(request)
    return redirect("userauths:sign-in")


# def activate_user(request, uidb64, token):
#     try:
#         uid = force_text(urlsafe_base64_decode(uidb64))
#         user = User.objects.get(pk=uid)

#     except Exception as e:
#         user = None

#     if user and generate_token.check_token(user, token):
#         user.is_email_verified = True
#         user.save()

#         messages.warning(request, "Email verified, you can now login.")
#         return redirect("userauths:sign-in")
    
#     return render(request, 'userauths/activate-failed.html',{'user': user})