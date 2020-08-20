from django.shortcuts import render, HttpResponse, HttpResponseRedirect, Http404
from .models import User, Role
from .forms import LoginUserForm


def index(request):
    user = User.objects.all()
    return render(request, 'index.html', {'user': user})


def login(request):
    """ form = LoginUserForm()
    if request.method == 'GET':
        raise Http404('Only POSTs are allowed')
    try:
        m = User.objects.get(username=request.POST.get('username'))
        if m.password == request.POST.get('password'):
            request.session['id_user'] = m.id
            return HttpResponseRedirect('/you-are-logged-in/')
    except User.DoesNotExist:
        return HttpResponse("Your username and password didn't match.") """
    return render(request, 'loginform.html')
