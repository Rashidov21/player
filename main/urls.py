from django.urls import path

from . import views
app_name = 'main'
urlpatterns = [
    path("", views.HomeView.as_view(), name='home'),
    path("login/",views.log_in, name='login'),
    path("logout/",views.log_out, name='logout'),
    path("about/", views.AboutView.as_view(), name='about'),
    path("contact/", views.Contact.as_view(), name='contact'),
    
    path('player/<slug:slug>', views.PlayerDetailView.as_view(), name='player_detail'),
    path('club/<str:name>', views.ClubListView.as_view(),name='club_list')
]
