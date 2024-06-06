# Para crear las urls debemos tomar en cuenta que tipo de view queremos agregar
# en el caso de las views basadas en funciones se pueden agregar pasando la funcion
# sin mas
from rest_framework.urls import path

# Importacion de las vistas
from . import views

urlpatterns = [

    path("user/", views.user_view, name="user"),
    path("user/<int:pk>/", views.user_detail_view, name="user_detail")

]