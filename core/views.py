from django.shortcuts import render,redirect
from django.views import View
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from google.auth.transport import requests
from google.oauth2 import id_token
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

class Home(View):
    def get(self,request):
            if request.user.is_authenticated:
                songs=Song.objects.all()
                return render(request,"home.html",{'songs':songs})
            else:
                return redirect("login")
    
class SongView(View):
    def get(self, request, id):
        if request.user.is_authenticated:
            song = Song.objects.get(id=id)
            song_list = list(Song.objects.all())
            favorites = Favoirite.objects.filter(song=song, user=request.user)
            l1=[]
            song_id = None 
            if favorites:
                for i in favorites:
                    l1.append(i.song.name)
                    song_id=i.id
            song_index = song_list.index(song)  
            return render(request, "song.html", {"song": song, "song_list": song_list, "song_index": song_index,"l1":l1,"song_id":song_id})
        else:
            return redirect("login")

class RegisterView(View):
    def get(self,request):
        return render(request,"register.html")
    
    def post(self,request):
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        user=User(username=username,email=email)
        user.set_password(password)
        user.save()
        return redirect("home")

class LoginView(View):
    def get(self,request):
        return render(request,"login.html")
    
    def post(self,request):
        username=request.POST['username']
        password=request.POST['password']

        user=authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect("home")
        
class AddSongView(View):
    def get(self,request):
        if request.user.is_authenticated:
            return render(request,"add_song.html")
        else:
            return redirect("login")
    
    def post(self,request):
        if request.user.is_authenticated:
            music_file=request.FILES['music']
            name=request.POST['name']
            add=Song(name=name)
            add.music.save(music_file.name, music_file)
            add.save()
            return redirect("home")
        else:
            return redirect("login")
   
@login_required
def LogoutView(request):
    logout(request)
    return redirect("login")

class FavouriteView(View):
    def get(self,request):
        if request.user.is_authenticated:
            favorites = Favoirite.objects.filter(user=request.user)
            return render(request,"favoirite.html",{"favorites":favorites})
        else:
            return redirect("login")

class FavouriteSongView(View):
    def get(self, request, id):
        if request.user.is_authenticated:
            favorite = Favoirite.objects.get(id=id)
            song_list = list(Favoirite.objects.all())  
            song_index = song_list.index(favorite)
            return render(request, "favoiritesong.html", {"song": favorite.song, "song_list": song_list, "song_index": song_index,"favorite":favorite.id})
        else:
            return redirect("login")

class AddToFavoritesView(View):
    def post(self, request, id):
        if request.user.is_authenticated:
            song = Song.objects.get(id=id)
            favorite = Favoirite(user=request.user, song=song)
            favorite.save()
            return redirect("home")
        else:
            return redirect("login")

@login_required
def deleteview(request,id):
        song=Favoirite.objects.get(id=id)
        song.delete()
        return redirect("home")

@csrf_exempt 
def google_signup(request):
    if request.method == 'POST':
        token = request.POST.get('id_token')
        try:
            id_info = id_token.verify_oauth2_token(token, requests.Request(), settings.GOOGLE_CLIENT_ID)
            email = id_info['email']
            name = id_info['name']
            user = authenticate(request, username=email, password=None)
            if user is not None:
                login(request, user)
            return redirect('home')  
        except ValueError:
            return redirect('login') 
    return redirect('login') 