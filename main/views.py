from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from django.core.mail import EmailMessage
from django.utils import timezone
from django.urls import reverse
from .models import *

@login_required
def Home(request):
    return render(request, 'index.html')

def kset(request):
    return render(request, 'kset.html')

def ksds(request):
    return render(request, 'ksds.html')

def kst(request):
    return render(request, 'kst.html')

def kss(request):
    return render(request, 'kss.html')

def ksp(request):
    return render(request, 'ksp.html')

def kamc(request):
    return render(request, 'kamc.html')

def kspr(request):
    return render(request, 'kspr.html')

def ksn(request):
    return render(request, 'ksn.html')

def ksc(request):
    return render(request, 'ksc.html')

def ksbm(request):
    return render(request, 'ksbm.html')

def GalleryView(request):
    return render(request, 'gallery.html')

def FestivalView(request):
    return render(request, 'festival.html')

def AboutView(request):
    return render(request, 'about.html')

def FacilitiesView(request):
    return render(request, 'facilities.html')


def AcademicView(request):
    return render(request, 'academic.html')

def TechnoView(request):
    return render(request, 'techno.html')

def ScienceView(request):
    return render(request, 'science.html')

def HealthView(request):
    return render(request, 'health.html')

def NursingView(request):
    return render(request, 'nursing.html')

def CommerceView(request):
    return render(request, 'commerce.html')

def HumanityView(request):
    return render(request, 'humanity.html')

def RegisterView(request):

    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user_data_has_error = False

        if User.objects.filter(username=username).exists():
            user_data_has_error = True
            messages.error(request, "Username already exists")

        if User.objects.filter(email=email).exists():
            user_data_has_error = True
            messages.error(request, "Email already exists")

        if len(password) < 5:
            user_data_has_error = True
            messages.error(request, "Password must be at least 5 characters")

        if user_data_has_error:
            return redirect('register')
        else:
            new_user = User.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                email=email, 
                username=username,
                password=password
            )
            messages.success(request, "Account created. Login now")
            return redirect('login')

    return render(request, 'register.html')



def LoginView(request):

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            return redirect('home')
        
        else:
            messages.error(request, "Invalid login credentials")
            return redirect('login')

    return render(request, 'login.html')

def LogoutView(request):

    logout(request)

    return redirect('login')

def ForgotPassword(request):
    # def ForgotPassword(request):
    if request.method == "POST":
        email = request.POST.get('email')

        try:
            user = User.objects.get(email=email)

            # Create a new password reset request
            new_password_reset = PasswordReset(user=user)
            new_password_reset.save()

            password_reset_url = reverse('reset-password', kwargs={'reset_id': new_password_reset.reset_id})
            full_password_reset_url = f'{request.scheme}://{request.get_host()}{password_reset_url}'

            email_body = f'Reset your password using the link below:\n\n\n{full_password_reset_url}'
            email_message = EmailMessage(
                'Reset your password',
                email_body,
                settings.EMAIL_HOST_USER,
                [email]
            )
            email_message.fail_silently = False  
            email_message.send()

            messages.success(request, "Password reset email has been sent.")
            return redirect('password-reset-sent', reset_id=new_password_reset.reset_id)

        except User.DoesNotExist:
            messages.error(request, f"No user with email '{email}' found")
            return redirect('forgot-password')

        except Exception as e:
            messages.error(request, f"An error occurred: {str(e)}")
            return redirect('forgot-password')

    return render(request, 'forgot_password.html')
def PasswordResetSent(request, reset_id):

    if PasswordReset.objects.filter(reset_id=reset_id).exists():
        return render(request, 'password_reset_sent.html')
    else:
       
        messages.error(request, 'Invalid reset id')
        return redirect('forgot-password')

def ResetPassword(request, reset_id):
    try:
        password_reset = PasswordReset.objects.get(reset_id=reset_id)
    except PasswordReset.DoesNotExist:
        messages.error(request, 'Invalid reset ID.')
        return redirect('forgot-password')

    # Check expiration time
    expiration_time = password_reset.created_when + timezone.timedelta(minutes=10)
    if timezone.now() > expiration_time:
        password_reset.delete()
        messages.error(request, 'Reset link has expired.')
        return redirect('forgot-password')

    if request.method == 'POST':
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, 'Passwords do not match.')
            return redirect('reset-password', reset_id=reset_id)

        if len(password) < 5:
            messages.error(request, 'Password must be at least 5 characters long.')
            return redirect('reset-password', reset_id=reset_id)

        # Reset password
        user = password_reset.user
        user.set_password(password)
        user.save()
        password_reset.delete()

        messages.success(request, 'Password reset successfully! Please log in.')
        return redirect('login')

    return render(request, 'reset-password.html') 