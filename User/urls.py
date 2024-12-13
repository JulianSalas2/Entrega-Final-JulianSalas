from django.urls import path
from AppCoder import views
from User import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    
    path('login/',views.login_request, name='login'),
    path('register/',views.register, name='register'),
    path('cerrar_sesion/', views.cerrar_sesion, name='cerrar_sesion'),
    path('editar_usuario/', views.editar_perfil, name="editar_usuario"),
    path('eliminar_avatar/', views.eliminar_avatar, name='eliminar_avatar'),
    path('agregar_avatar/', views.agregar_avatar, name='agregar_avatar'),


    
]