from django.urls import path
from . import views

app_name = "courses"

urlpatterns = [
    path('', views.course_list, name='course_list'),
    path('<int:course_id>/', views.course_detail, name='course_detail'),
    path('<int:course_id>/video/<int:video_id>/', views.video_detail, name='video_detail'),
]
