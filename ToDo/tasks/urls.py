from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('login/', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.sign_out, name='logout'),
    path('add_task/', views.new_task, name='add_task'),
]
