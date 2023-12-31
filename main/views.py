from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView,DetailView
from .models import Country, Player, Club
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout




def log_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.get(username=username)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login( request, user)
            return redirect('main:home')
    context = {}
    return render(request, "log_in.html", context)

def log_out(request):
    logout(request)
    return redirect('main:home')



# def HomeView(request):
#     if request.GET.get('q') != None:
#         q = request.GET.get('q')
#     else:
#         q = ' '
#     player = Player.objects.filter(
#         name__icontains = q
#     )
#     count = player.count()    
#     context = {"player":player}
#     return render(request, "index.html", context)
#     print(player)





class HomeView(ListView):
    model = Player
    template_name = 'index.html'
    context_object_name = 'players'
    paginate_by = 4
    # context_object_name = {"play÷er", "image"}
    
    def get_queryset(self):
        player = Player.objects.all()
        return player
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["clubs"] = Club.objects.all()
        return context

class PlayerDetailView(DetailView):
    model = Player


class ClubListView(ListView):
    model = Player
    template_name = "index.html"
    paginate_by = 3
    
    def get_queryset(self):
        print(self.request.body)
        return Player.objects.all()
    
    
    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context["object_list"] = Player.objects.filter(name=kwargs.get("name"))
       return context
   
    
    

class AboutView(TemplateView):
    template_name = 'about.html'
class Contact(TemplateView):
    template_name = 'contact.html'
    
# Create your views here.