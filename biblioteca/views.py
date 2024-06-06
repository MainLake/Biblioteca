# Vistas basadas en funciones

# Decorador encargado de hacer que la funcion se comporte como una vista
from rest_framework.decorators import api_view

# Importacion del metodo Response para responder a las peticiones
from rest_framework.response import Response

# Importacion del metodo para definir los status code de las respuestas
from rest_framework import status

# Importacion de los modelos
from .models import User

# Importacion de los serializadores
from .serializers import UserSerializer

# Los metodos o peticiones que que reciben una parametro dinamico deben
# de estar separados debido a la naturaleza de recibir un parametro en la url

# El obtener todos los elementos no requiere especificar nada en las url debido
# a que este no recibe ningun parametro en la url


@api_view(["GET", "POST"])
def user_view(request):

    if request.method == "GET":

        users = User.objects.all()

        # Para serializar la informacion recibida de una query en el orm de django
        # se debe pasar la queryset al serializador como un parametro mas, si es mas de un
        # registro se debe de indicar pasandole una variable many = true
        user_serializer = UserSerializer(users, many=True)

        users_data = user_serializer.data

        return Response({
            "data": users_data
        }, status=status.HTTP_200_OK)

    if request.method == "POST":

        user_request_data = request.data

        # Podemos deserializar la informacion de tal manera que recibamos informacion
        # de tipo json o xml para poder traducir esa informacion a datos legibles por python
        # Este proceso se lleva a cabo por el serializador y se pasa la informacion por medio de la variable data
        user_serializer = UserSerializer(data=user_request_data)

        # Cuando realizamos este proceso de deserealizar debemos validar si la informacion recibida en la data de la request es correcta
        # de lo contrario no podremos conrinuar manejando el serializador
        if user_serializer.is_valid():
            user_serializer.save()
            return Response({
                "data": user_serializer.data
            }, status=status.HTTP_201_CREATED)
        else:
            print(user_serializer.errors)
            return Response({
                "data": {
                    "error": {
                        "message": "Ha ocurrido un error al crear a el usuario",
                        "details": user_serializer.errors
                    }
                }

            }, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT"])
def user_detail_view(request, pk=None):

    if request.method == "GET":

        user = User.objects.filter(pk=pk).first()

        if user is None:
            return Response({
                "data": {
                    "error": {
                        "message": "No existe el usuario"
                    }
                }
            }, status=status.HTTP_404_NOT_FOUND)

        # Serializamos la informacion
        user_serializer = UserSerializer(user)

        return Response({
            "data": user_serializer.data
        }, status=status.HTTP_200_OK)

    if request.method == "PUT":

        user = User.objects.filter(pk=pk).first()
        user_data_request = request.data

        if user is None:
            return Response({
                "data": {
                    "error": {
                        "message": "No existe el usuario"
                    }
                }
            }, status=status.HTTP_404_NOT_FOUND)

        user_serializer = UserSerializer(user, user_data_request)

        if not user_serializer.is_valid():
            return Response({

                "data": {
                    "error": {
                        "message": "Datos no validos para actualizar a el usuario",
                        "details": user_serializer.errors
                    }
                }
            }, status=status.HTTP_400_BAD_REQUEST)

        return Response({
            "data": user_serializer.data            
        }, status=status.HTTP_202_ACCEPTED)