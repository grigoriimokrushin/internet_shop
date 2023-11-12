from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'index.html')


def contacts(request):
    return render(request, 'contacts.html')
