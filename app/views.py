from django.contrib.auth.models import User, Group
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as auth_login
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
from app.models import CustomGroup


def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "login.html")


@csrf_exempt
def login(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        group = None
        if user is not None:
            auth_login(request, user)
            group = CustomGroup.objects.get(customuser__user=request.user)  # request.user.id
    return render(request, "result.html", {'group': group})
