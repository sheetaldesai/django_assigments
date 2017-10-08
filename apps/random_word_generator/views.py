## -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

# the index function is called when root is visited
def index(request):
    return render(request,'random_word_generator/index.html')

def generate(request) :
    unique_id = get_random_string(length=14)
    print unique_id
    if request.method == "POST" :
        print request.POST
        if 'generate' in request.POST :
            print "printing session"
            print request.session
            if "attempt" in request.session :
                attempt = request.session["attempt"] + 1
            else :
                attempt = 1
            request.session["random"] = unique_id
            request.session["attempt"] = attempt 
        elif 'reset' in request.POST :
              request.session.flush()
              print "Session flushed"
    return redirect("/random_word")

def reset(request) :
    
    if request.method == "POST" :
        request.session.flush()
    return redirect("/random_word")
