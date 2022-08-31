from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from .models import Game
from chess import STARTING_FEN

def index(request): 
    print(request.GET)
    if request.method == 'GET':
        if request.GET.get('online'):
            Game.objects.create(fen=STARTING_FEN) 
            total = Game.objects.latest('pk').pk
            # Game.objects.create(fen=STARTING_FEN, white=1234, black=1234)
            # if request.GET.get('computer'):
            #     Game.objects.create(fen=STARTING_FEN)   
            # else if request.GET.get('mybtn2'):
            return redirect('/%d' % total)
    return render(request, 'chessapp/index.html')
def game(request, game_id):
    if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest' and request.method == "POST":
        Game.objects.filter(pk=game_id).update(fen=request.POST['fen'])
        print(request.POST['fen'])
        print(Game.objects.get(pk=game_id).fen, "new fen")
        return HttpResponse("Success!")
    fen = Game.objects.get(pk=game_id).fen
    return render(request,'chessapp/game.html', {'fen': fen})
def register(request):
    if request.method == 'POST':
        print(request.POST)
        username, password, email = request.POST['username'], request.POST['email'], request.POST['password']
        if User.objects.filter(username=username).exists():
            print('NOT OK: USERNAME EXISTS')
        elif User.objects.filter(email=email).exists():
            print('NOT OK: EMAIL EXISTS')
        else:
            user = User.objects.create_user(username, email, password)
            print('OK OK user created')
    return render(request, 'chessapp/register.html')
def login_view(request):
    if request.method == 'POST':
        print(request.POST)
        username, password = request.POST['username'],  request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('/')
        else:
            print('NOT OK BAD AUTH')
    return render(request, 'chessapp/login.html')
def logout_view(request):
    logout(request)
    return redirect('/')
