from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('gigs/<int:id>/', views.gig_detail, name='gig_detail'),
    path('favorite/<int:gig_id>/', views.toggle_favorite, name='toggle_favorite'),
    path('dashboard/provider/', views.provider_dashboard, name='provider_dashboard'),
    path('dashboard/seeker/', views.seeker_dashboard, name='seeker_dashboard'),
    path('post/', views.post_gig, name='post_gig'),
]