# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect

# the index function is called when root is visited
def index(request):
    response = "Placeholder to later display all the list of blogs"
    return HttpResponse(response)


# Create your views here.
def new(request):
    response = "placeholder to display a new form to create a new blog"
    return HttpResponse(response)

def create(request): 
    return redirect('/blog') 

def show(request, num):
    response = "'placeholder to display blog ", num
    return HttpResponse(response)

def edit(request, num):
    response = "'placeholder to edit blog ", num
    return HttpResponse(response)

def destroy(request, num):
    return redirect('/blog') 