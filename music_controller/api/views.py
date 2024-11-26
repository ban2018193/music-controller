from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def main(request):
    ''' This function creates a response from endpoints'''
    return HttpResponse('<h1>hi</h1>')
