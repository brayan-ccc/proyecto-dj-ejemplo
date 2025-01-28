from django.urls import path
from . import views

urlpatterns = [
    path('bienvenida/', views.bienvenida, name='bienvenida' ),
    path('saludo/<str:nombre>/',views.saludo, name='saludo'),
    path('bienvenida_clase/',views.BienvenidaVista.as_view(), name='bienvenida_clase'),   
]
