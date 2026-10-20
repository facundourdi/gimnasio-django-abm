from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Autenticación
    path('registro/', views.registrar_usuario, name='registro'),
    path('login/', auth_views.LoginView.as_view(template_name='miembros/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # ABM
    path('', views.listar_miembros, name='listar_miembros'),
    path('nuevo/', views.alta_miembro, name='alta_miembro'),
    path('editar/<int:pk>/', views.editar_miembro, name='editar_miembro'),
    path('eliminar/<int:pk>/', views.baja_miembro, name='baja_miembro'),
]