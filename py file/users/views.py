from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .models import Gig
from .forms import GigForm

def home(request):
    gigs = Gig.objects.all()
    return render(request, 'users/home.html', {'gigs': gigs})

def gig_detail(request, id):
    gig = get_object_or_404(Gig, id=id)
    return render(request, 'users/gig_detail.html', {'gig': gig})

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

def provider_dashboard(request):
    gigs = Gig.objects.filter(created_by=request.user)
    return render(request, 'users/provider_dashboard.html', {'gigs': gigs})

def seeker_dashboard(request):
    favorites = request.user.favorite_gigs.all()
    return render(request, 'users/seeker_dashboard.html', {'favorites': favorites})

def toggle_favorite(request, gig_id):
    gig = get_object_or_404(Gig, id=gig_id)
    if request.user in gig.favorited_by.all():
        gig.favorited_by.remove(request.user)
    else:
        gig.favorited_by.add(request.user)
    return redirect('home')

def post_gig(request):
    if request.method == 'POST':
        form = GigForm(request.POST)
        if form.is_valid():
            gig = form.save(commit=False)
            gig.created_by = request.user
            gig.save()
            return redirect('gig_detail', id=gig.id)
    else:
        form = GigForm()
    return render(request, 'users/post_gig.html', {'form': form})