from email import message
from rest_framework.response import Response
import imp
from multiprocessing import context
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render , redirect , HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from student.models import Student
import jwt, datetime
# Create your views here.
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404

from student.form import StdForm
def home(request):
  
    try:
        user = request.user
        fname = user.first_name
        list_question = Student.objects.all()
        context = {
        "fname": fname,
        "dsquest": list_question

        }
       
    except:
        # user = request.user
        # id = user.first_name
        list_question = Student.objects.all()
        
        context = {

        "dsquest": list_question
      
        }
       
    return render(request, "authentication/index.html", context)

    

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if User.objects.filter(username = username):
            messages.error(request, "Tên người dùng đã tồn tại !")
            return redirect('signup')


        if User.objects.filter(email = email):
            messages.error(request, "Email đã đăng ký !! ")
            return redirect('signup')

        if len(username)>10:
            message.error(request, "Tên người dùng phải dưới 10 ký tự")

        if pass1 != pass2:
            messages.error(request,"Pass không trùng nhau")

        if not username.isalnum():
            messages.error(request,"username phải là chữ và số")
            return redirect("signup")

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()

       
    return render(request, "authentication/signup.html")

def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        pass1 = request.POST['pass1']
        user = authenticate(username= username, password = pass1)

        if user is not None:
            login(request, user)
            fname = user.first_name
            context = {"fname" :fname}
            # return render(request, "authentication/index.html", context)
            return HttpResponseRedirect("/" ,context)
        else:
            messages.error(request, "Thất bại! bạn kiểm tra lại tài khoản - Mật khẩu")
            return redirect('home')
    return render(request, "authentication/signin.html")

def signout(request):
    logout(request)
    messages.success(request, "Đăng xuất thành công")
    return redirect('home')
def view(request):
    list_question = Student.objects.all()
    context = {"dsquest": list_question}
    
    # return render(request, "polls/question_list.html",context)
    return render(request, "authentication/index.html",context)


def ADD(request):
    # context ={}
    # form = StdForm(request.POST or None)
    # if form.is_valid():
    #     form.save()
    #     return HttpResponseRedirect("/")
    # context['form']= form
    if request.method == "POST":
        student_name  =request.POST.get('student_name')
        student_age  =request.POST.get('student_age')
        student_cccd =request.POST.get('student_cccd')
        student_email =request.POST.get('student_email')
        student_sex  =request.POST.get('student_sex')
        student_class =request.POST.get('student_class')
        student_address =request.POST.get('student_address')
        student_img  =request.POST.get('student_img')

        std = Student(
            student_name  = student_name,
            student_age  = student_age,
            student_cccd = student_cccd,
            student_email = student_email,
            student_sex  = student_sex,
            student_class = student_class,
            student_address = student_address,
            student_img  = student_img
        )
        std.save()
        return redirect('home')

def edit(request):
    std = Student.objects.all()
    context = {
        "std": std
    }
    return (request, 'index.html', context)
def update(request, id):
    if request.method == "POST":
        student_name  =request.POST.get('student_name')
        student_age  =request.POST.get('student_age')
        student_cccd =request.POST.get('student_cccd')
        student_email =request.POST.get('student_email')
        student_sex  =request.POST.get('student_sex')
        student_class =request.POST.get('student_class')
        student_address =request.POST.get('student_address')
        student_img  =request.POST.get('student_img')

        std = Student(
            id = id,
            student_name  = student_name,
            student_age  = student_age,
            student_cccd = student_cccd,
            student_email = student_email,
            student_sex  = student_sex,
            student_class = student_class,
            student_address = student_address,
            student_img  = student_img
        )
        std.save()
        return redirect('home')
    return (request, 'index.html')

def delete(request,id):
    std = Student.objects.filter(id = id)
    std.delete()
    return  redirect("home")