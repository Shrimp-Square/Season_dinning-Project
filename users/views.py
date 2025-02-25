from django.shortcuts import render,redirect
from users.forms import LoginForm, SignupForm
from django.contrib.auth import authenticate, login, logout
from users.models import User
from django.urls import reverse 

# Create your views here.

def login_view(request):
    if request.user.is_authenticated:
        return render(request, "index.html")
    
    if request.method == "POST":
        form = LoginForm(data = request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
    
            user = authenticate(username=username, password=password)

            if user:
                login(request,user)
                return render(request, "index.html")
            else:
                form.add_error(None, "해당 사용자가 존재하지 않습니다")

        context = {"form":form}
        return render(request, "users/login.html", context)
    
    else:
        form = LoginForm()
        context = {"form": form}
        return render(request, "users/login.html", context)
    

def logout_view(request):
    logout(request)

    return redirect("/users/login/")

def signup_view(request):
    if request.method == "POST":
        form = SignupForm(data = request.POST, files = request.FILES)

        # Form이 유효하면 form.save() 메서드로 사용자 생성
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/")
        
    # GET 요청에서는 빈 form 을 보여줌
    else:
        #  SignupForm 인스턴스 생성, Template에 전달
        form = SignupForm()

    # context로 전달되는 form은 두가지 경우 존재
    # POST 요청에서 생성된 form이 유효하지 않은 경우, GET 요청으로 빈 form이 생성된 경우 
    context = {"form":form}
    return render(request, "users/signup.html", context)


