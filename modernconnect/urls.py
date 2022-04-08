from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('skills/', views.skills, name="skills"),
    path('register/', views.register, name="register")
]