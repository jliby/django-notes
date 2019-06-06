from django.shortcuts import render
from django.http import Httpresponse
# Create your views here.
def homePageView(request):
    return HttpResponse('Hello World')