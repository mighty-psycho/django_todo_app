from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from reset_password.forms import ResetPassCheckEmail


urlpatterns = [
    path('', include('todo.urls')),
    path('admin/', admin.site.urls),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='reset_password/password_reset.html',
         form_class=ResetPassCheckEmail,
         email_template_name='reset_password/password_reset.txt',
         subject_template_name='reset_password/password_reset_subject.txt'),
         name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(
        template_name='reset_password/password_reset_done.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='reset_password/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='reset_password/password_reset_complete.html'),
         name='password_reset_complete'),
]
