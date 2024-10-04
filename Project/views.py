from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import UserSignUpForm
from .models import UserDetails
from django.contrib.auth import login, logout, authenticate

def userinfo_view(request):
  if request.user.is_authenticated:
    return render(request, 'Project/UserInfo.html', {'userinfo': request.user})
  else:
    return redirect('login_view')

def login_view(request):
  if request.method == "POST":
    username = request.POST["username"]
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
      login(request, user)
      return redirect('userinfo_view')
  return render(request, 'Project/Login.html')

def signup_view(request):
  if request.method == 'POST':
    form = UserSignUpForm(request.POST)
    if form.is_valid():
      email = form.cleaned_data['email']
      if User.objects.filter(email=email).exists():
        return redirect('login_view')
      else:
        userinfo = form.save()
        user = authenticate(request,username=user_name, password = request.POST['password'])
        login(request, user)
        return redirect('userinfo_view')
  else:
    form = UserSignUpForm()
  return render(request, 'Project/Signup.html', {'form' : form})

def logout_view(request):
  logout(request)
  return redirect('login_view')
  
def page_view(request):
  return render(request, 'Project/Page.html')
