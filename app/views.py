from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
# from . models import Person, Students
from .forms import *
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.exceptions import ValidationError
# # Create your views here.


#@login_required(login_url='login')
def home(request):
    dynastu = Student.objects.all()
    context = { 'dyna': dynastu}
    return render(request, 'home.html', context)


def update(request, id):  # GET#PUT#POST
    z = Student.objects.get(pk=id)
    form = StudentForm(instance=z)  # old data
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=z)
        if form.is_valid():
            form.save()
            return redirect('/app/home/')
    context = {'form': form}
    return render(request, 'update.html', context)


def delete(request, id):
    Student.objects.get(pk=id).delete()
    messages.info(request, "data deleted")
    return render(request, 'delete.html')
    # return redirect('/app/home')


def read(request, id):
    print(id)
    dynamicdata = Student.objects.get(pk=id)
    context = {'dynamic': dynamicdata}
    return render(request, 'read.html', context)

#     # return HttpResponse('This is a read fuction')


def create(request):  # POST
    form = StudentForm()
    if request.method == 'POST': 
        form = StudentForm(request.POST)
        if form.is_valid():
            #var =form.save(commit=False)
            stud = form.cleaned_data['name'].lower()
            sub = form.cleaned_data['subject'].lower()
            if Student.objects.filter(name=stud, subject=sub).exists():
                messages.info(request, "data exists")
                return render(request, 'create.html',{'form': form})
            else:
                form.save()
            return redirect("/app/home/")

    context = {'form': form}
    return render(request, 'create.html', context)


def signup(request):
    form = SignupForm()
    if request.method == 'POST':  # TRUE
        print(request.POST)
        form = SignupForm(request.POST)
        if form.is_valid():
            # breakpoint()
            form.save()
    context = {'form': form}
    return render(request, 'signup.html', context)


def loginn(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if request.user.is_authenticated:
                username = request.user.username
                messages.info(request, "Welcome "+username)
            return redirect('/app/home')
    return render(request, 'login.html')


def logoutt(request):  # get
    logout(request)
    return redirect('/')
