from django.shortcuts import render
from django.template import loader

def index(request):
    template = loader.get_template('index.html')
    # context = {
    #     'latest_question_list': latest_question_list,
    # }
    return render(request, 'index.html') #HttpResponse(template.render(context, request))
