from django.shortcuts import render,redirect

def main(request):
    return render(request, 'riddles/landing_page.html')
