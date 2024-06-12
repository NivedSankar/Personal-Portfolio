
from django.shortcuts import render,redirect
from mywebsite.settings import EMAIL_HOST_USER
from django.contrib import messages
from django.core.mail import send_mail
from django.http import HttpResponse
from .models import *
# from .forms import *

# Create your views here.

def index(request):
    return render(request,'index.html')


def message(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        user_message = request.POST.get('message')

        email_subject = f"{subject}"
        email_message = f"Hi, I'm {name}\n\n{user_message}"

        email_from = email
        recipient_list = ['nivedsankarpm7@gmail.com']

        try:
            send_mail(email_subject, email_message, email_from, recipient_list)
            messages.success(request, 'Your message has been sent successfully!')
        except Exception as e:
            messages.error(request, f'There was an error sending your message. Error: {e}')

        print(name)

        return redirect('index')

    return render(request, 'index.html')


