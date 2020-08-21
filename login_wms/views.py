from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect
from .models import User, Role
from .forms import LoginUserForm


def index(request):
    user = User.objects.all()
    return render(request, 'index.html', {'user': user})


def loginform(request):
    if request.method == 'POST':
        m = User.objects.get(username=request.POST['username'])
        password = request.POST['password']
        if m.password == password:
            return redirect('home')
        else:
            return redirect('login')

    return render(request, 'loginform.html')


""" def login(request):
    if request.method == "GET":
        if (Users.objects.filter(username = request.GET.get("username"), password = request.GET.get("password"))).exists():
            user = Users.objects.get(username = request.GET.get("username"), password = request.GET.get("password"))
            request.session["id_user"] = user.id
            # request.session.set_expiry(10)
            # it shows home page
            return redirect('home')
    #it shows again login page
    return render(request,"loginform.html") """

""" if request.method == 'POST':
        m = User.objects.get(username=request.POST['username'])
        if m.password == request.POST['password']:
            return redirect('home')
        else:
            return redirect('login') """
