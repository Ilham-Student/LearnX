from django.urls import path
from . import views

app_name = 'core'   # 🔥 this registers the namespace

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'),
]
