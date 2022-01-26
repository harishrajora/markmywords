from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from .models import UserTable, WordMeaning
import requests
import json
# Create your views here.

def index(request):
    return render(request, 'index.html')

def loginpage(request):
    return render(request, 'login.html')

def loginuser(request):
    if(request.method == 'GET'):
        print('You might want to sign in first')
        return render(request, 'login.html',{'signin_error' : 'Direct Access Not Allowed'})
    else:
        user = authenticate(request, username = request.POST.get('username'), password = request.POST.get('userpassword'))
        if user is None:
            print('Wrong Credentials')
            return render(request, 'login.html', {'signin_error': 'Wrong Credentials or User is not registered!!'})
        else:
            login(request, user)
            print("Login : Success")
            return redirect('dashboard')

def logoutuser(request):
    logout(request)
    return redirect('index')

def signup(request):
    print("Signup Entered")
    if request.method == 'GET':
        return render(request, 'index.html')
    else:
        if User.objects.filter(username = request.POST.get('username')).exists():
            print("Username Already Exists")
            return render(request, 'login.html', {'signup_error' : 'Username Already Exists'})

        elif User.objects.filter(email = request.POST.get('useremail')).exists():
            print("Email Already Exists")
            return render(request, 'login.html', {'signup_error' : 'Email Already Exists'})

        else:
            user = User.objects.create_user(request.POST.get('username'), email = request.POST.get('useremail'), first_name = request.POST.get('name'), password = request.POST.get('userpassword'))
            user.save()
            return render(request, 'login.html', {'signup_error' : 'User Created Successfully'})

def dashboard(request):
    if(not UserTable.objects.all().filter(username = request.POST.get('username')).exists()):
        print("User not found")
        return render (request, 'dashboard.html', {'error' : 'user_not_found'})
    UserTable_obj = UserTable.objects.all().filter(username = request.POST.get('username'))
    return render(request, 'dashboard.html', {'error', 'user_found'})

def search_word_page(request):
    return render(request, "search_words.html")

def save_the_word(request):
    WordMeaning_obj = WordMeaning()
    WordMeaning_obj.word = request.POST['word']
    WordMeaning_obj.meaning = request.POST['word']
    WordMeaning_obj.username = request.user
    return HttpResponse("success")


def search_word(request):
    response = requests.get("https://api.dictionaryapi.dev/api/v2/entries/en/"+request.POST['word'])
    response = json.loads(response.text)
    print(response)
    meaning = response[0]['meanings'][0]['definitions'][0]['definition']
    return HttpResponse(meaning)
