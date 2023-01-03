from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.


def index(request):

    pagina = loader.get_template('index.html')
    loadpage = pagina.render({'nombre':'jhon'}) 
    return HttpResponse(loadpage)

def cliente(request):

    pagina = loader.get_template('index.html')
    loadpage = pagina.render({'nombre':'jhon'}) 
    return HttpResponse(loadpage)
