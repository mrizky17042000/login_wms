from django.shortcuts import render
from .models import User, Role


def index(request):
    user = User.objects.all()
    return render(request, 'index.html', {'user': user})
