from django.urls import path

from . import views
app_name = 'main'
urlpatterns = [
    path("", views.HomeView, name='home'),
    path("login/",views.log_in, name='login'),
    path("logout/",views.log_out, name='logout'),
    path("about/", views.AboutView.as_view(), name='about'),
    path("contact/", views.Contact.as_view(), name='contact')
]
