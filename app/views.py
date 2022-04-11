from django.shortcuts import render
from .models import Clients


def home(request):
    clients = Clients.objects.all()
    context = {'clients':clients}
    return render(request, 'app/home.html', context)