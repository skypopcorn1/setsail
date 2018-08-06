from .forms import ClubRegistrationForm
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.template import loader


def index(request):
    template = loader.get_template('index.html')
    form = ClubRegistrationForm
    context = { 'form': form}
    return render(request, 'index.html', context) #HttpResponse(template.render(context, request))

def clubRegistration(request):
    template = loader.get_template('register.html')
    form = ClubRegistrationForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = { 'form': form}
    return render(request, 'register.html', context)
