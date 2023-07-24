from typing import Optional
from django.shortcuts import render, redirect
from .forms import FormRegisterArtist, FormLoginArtist
from .models import ArtistProfile
from django.contrib import messages
from django.contrib.auth.views import LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import authenticate, login
from django.views.generic import ListView, DetailView, UpdateView
from django.contrib.auth import get_user_model


def register_artist_view(request):
    """ Saves details of new members in the database """
    if request.method == 'POST':
        form_instance = FormRegisterArtist(request.POST)
        if form_instance.is_valid():
            first = form_instance.cleaned_data.get('first_name')
            form_instance.instance.username = form_instance.cleaned_data.get('email') # using email id for Username
            form_instance.save()
            messages.success(request, f"Artist {first} is created")
            return redirect('login')
        else:
            messages.error(request, form_instance.errors)
            context = {'memberform': FormRegisterArtist()}
            return render(request, 'Artist/create-member.html', context)
    else:
        context = {'memberform': FormRegisterArtist()}
        return render(request, 'Artist/create-member.html', context)



def artist_login_view(request):
    if request.method == 'POST':
        form_instance = FormLoginArtist(request.POST)
        if form_instance.is_valid():
            em = form_instance.cleaned_data.get('email')
            pw = form_instance.cleaned_data.get('password')
            user = authenticate(request, username=em, password=pw)
            if user is not None:
                login(request, user)
                messages.success(request, f'User {em} logged-in')
                return redirect('gallery')
            else:
                messages.error(request, f"Login attempt failed for user {em}")                                       
                return redirect('login')
        else:
            messages.error(request, "Credentials invalid")      
            return redirect('login')  
    else:
        return render(request, 'Artist/login.html', {'form_login': FormLoginArtist()})



class ArtistLogout(SuccessMessageMixin, LogoutView):
    success_message = "You're logged-out"


class ViewAllArtists(LoginRequiredMixin, ListView):
    model = get_user_model()
    template_name = 'Artist/all_list.html'


class ViewOneArtist(LoginRequiredMixin, DetailView):
    model = get_user_model()
    template_name = 'Artist/artist_detail.html'

    

class UpdateArtistProfile(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    model = ArtistProfile
    fields = ['picture']
    

    def test_func(self):
        if self.request.user == self.get_object().nickname: # username & nickname both contain email
            return True
        return False
    
    success_message = 'Profile updated'


