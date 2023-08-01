from django import forms
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import viewsets, status, exceptions
from django.db import transaction
from rest_framework.exceptions import APIException
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from .models import Student

from .form import StdForm

# Create your views here.
def index(requet):

    return render(requet, "polls/index.html")

def view(request):
    list_question = Student.objects.all()
    context = {"dsquest": list_question}
    
    # return render(request, "polls/question_list.html",context)
    return render(request, "authentication/index.html",context)

def detail(request, id):
    try:
        s = Student.objects.get(pk=id)
        context = {"poll": s}
        return render(request, "polls/detail.html", context)
    except:
        return render(request, "polls/detail.html")

def update(request, id):
    try:
    
        context = {}
        obj = get_object_or_404(Student, id = id)
        form = StdForm(request.POST or None, instance = obj)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
        context["form"] = form
        context['obj'] = obj
        return render(request, "polls/detail.html", context)
    except:
        return render(request, "polls/detail.html")

def post(request, id):
    q = Student.objects.get(pk = id) 
    render(request, "polls/create.html", {"qs":q})
def create_view(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    form = StdForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
    context['form']= form
    return render(request, "polls/create_views.html", context)
def delete(request, id):
    context ={}
    obj = get_object_or_404(Student, id = id)
    if request.method =="POST":
        # delete object
        obj.delete()
        return HttpResponseRedirect("/")
 
    return render(request, "polls/delete.html", context)

