from django.urls import path
from todo import views

app_name = 'todo'

urlpatterns = [
    path('', views.todo, name='todo'),
    path('login/', views.login_user, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_user, name='logout'),
    path('delete/<int:id>', views.delete_todo, name='delete_todo'),
    path('update/<int:id>', views.update_todo, name='update_todo'),
    path('password/', views.change_password, name='update_password')
]
