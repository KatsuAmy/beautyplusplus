from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
from django.http import HttpResponse


def main(request):
    #template = loader.get_template('beautyplus/templates/test.html')
    context = {}
    return render(request,'test.html',context)
