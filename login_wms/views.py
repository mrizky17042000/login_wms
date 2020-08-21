from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect
from .models import User, Role
from .forms import LoginUserForm
from pprint import pprint

from django.contrib.auth.decorators import login_required


def index(request):
    if 'user_id' not in request.session:
        return redirect('home')
    else:
        user = User.objects.all()
        return render(request, 'index.html', {'user': user})


def about(request):
    if 'user_id' not in request.session:
        return redirect('home')
    else:
        return render(request, "about.html")


def loginform(request):
    if 'user_id' in request.session:
        return redirect('home')
    else:
        if request.method == 'POST':
            m = User.objects.get(username=request.POST['username'])
            password = request.POST['password']
            password2 = m.password
            pass_model = password2.split(" ")[0]
            if pass_model == password:
                request.session['user_id'] = m.id_user
                return redirect('home')
            else:
                return redirect('login')

    return render(request, 'loginform.html')


def logout(request):
    try:
        del request.session['user_id']
        return redirect('login')
    except KeyError:
        pass


""" if request.method == 'POST':
        m = User.objects.get(username=request.POST['username'])
        password = request.POST['password']
        password2 = m.password
        pass_model = password2.split(" ")[0]
        if pass_model == password:
            return redirect('home')
        else:
            return redirect('login')

    return render(request, 'loginform.html') """
