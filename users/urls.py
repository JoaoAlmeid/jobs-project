from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('cadastrar/', views.register_view, name='cadastro'),
    path('logout/', views.logout_view, name='sair'),
    path('login/', views.login_view, name='login')
]