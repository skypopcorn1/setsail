from datetime import datetime
from .forms import RaceForm, RegistrationForm, LoginForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, redirect
from django.template import loader
from race.models import (Race, RaceCourse)


def index(request):
    return render(request, 'index.html') #HttpResponse(template.render(context, request))

def home(request):
    return render(request, 'home.html')

def club(request):
    return render(request, 'club.html')

def RaceManagement(request):
    current_time = datetime.now()
    previous_races = Race.objects.filter(race_finish__lt=current_time)
    upcoming_races = Race.objects.filter(race_finish__gt=current_time)
    context = {'previous_races' : previous_races, 'upcoming_races' : upcoming_races }

    return render (request, 'racemanagement.html', context)

def RaceManagementAdd(request):
    form = RaceForm(request.POST or None, request.FILES or None)

    if request.method == 'POST' and form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        role = request.POST["user_role"]
        instance.user_role.set(role)
        return redirect("/home")
    else:
        context = { 'form': form}
        return render(request, 'addrace.html', context)

def registration(request):
    form = RegistrationForm(request.POST or None, request.FILES or None)

    if request.method == 'POST' and form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        role = request.POST["user_role"]
        print (role)
        instance.user_role.set(role)
        if str(role) in ["1", "2"]:
            return redirect("/club/home")
        elif str(role) in ["3","4","5"]:
            return redirect("/home")
        else:
            return HttpResponse("damn it!")
    else:
        context = { 'form': form}
        return render(request, 'register.html', context)

def LoginView(request):
    form = LoginForm(request.POST or None)
    context = {
        "form": form
    }
    # next_ =request.GET.get('next')
    # next_post =request.GET.get('next')
    # redirect_path = next_ or next_post or None
    if form.is_valid():
        email    = form.cleaned_data.get("email")
        password    = form.cleaned_data.get("password")
        user        = authenticate(request, email=email, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect("/")
        else:
            print("Error")
    return render(request, "login.html", context)
