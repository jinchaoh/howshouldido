from django.shortcuts import render

# Create your views here.
def show_index(request,category):
    
    print category
    return 