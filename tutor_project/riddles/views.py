from django.shortcuts import render
from .forms import email_form
from django.contrib import messages

def main(request):
    emailform = email_form()
    if request.method == 'POST':
        emailform = email_form(request.POST)
        if emailform.is_valid():
            email = emailform.cleaned_data['email']
            print(email)
            emailform = email_form()
            messages.error(request, 'Ваша заявка отправлена, скоро я с Вами свяжусь!')
    context ={
        'emailform':emailform,
    }
    return render(request, 'riddles/landing_page.html', context)

