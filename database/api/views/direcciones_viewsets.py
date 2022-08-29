
from rest_framework import viewsets, permissions
from rest_framework.response import Response


from database.models import Direcciones
from database.api.serializers import DireccionesSerializer
from database.api.permissions import GetOwnData
from .methods import CustomMethods
class DireccionesViewSet(viewsets.ModelViewSet, CustomMethods):
    queryset = Direcciones.objects.using('homebanking').all()
    serializer_class = DireccionesSerializer

    filter_id = ["titular_id"]
    def get_permissions(self):
        if self.action == "retrieve" or self.action == "list":
            permission_classes = [permissions.IsAuthenticated, GetOwnData]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]
    
    
    def list(self, request):
        # Cuentas del cliente
        if not request.user.is_staff == 1:
            customer_id = self.get_customer_id(self.request)
            data = self.queryset.filter(titular_id=customer_id) or [
                {"message": "El usuario solicitado no tiene direcciones registradas"}
            ]
        else:
            data = self.filter_queryset(self.get_queryset())

        # corroboramos si llegó informacion
        if len(data) > 0 and type(data[0]) == dict: 
            return Response(data)
        else:
            serializer = self.get_serializer(data, many=True)
            return Response(serializer.data)
    
    def post(self,request, *args, **kwargs):
        data = request.data
        serializer = DireccionesSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, dir_id): 
        direccion = Direcciones.objects.filter(pk=dir_id).first()
        if direccion:
            serializer = DireccionesSerializer(direccion)
            direccion.delete()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND) 
    
    def put(self, request, dir_id):
        direccion = Direcciones.objects.filter(pk=dir_id).first()
        serializer = DireccionesSerializer(direccion)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

""" from ..serializers import DireccionesSerializer
from ...models import Direcciones

from rest_framework.views import APIView 
from rest_framework.response import Response 
from rest_framework import status
from django.db import models



class DireccionesList(APIView):
    serializer_class= DireccionesSerializer
    queryset = Direcciones.objects.using("homebanking").all()
    def get(self,request):
        direcciones = Direcciones.objects.using('homebanking').all()
        serializer = DireccionesSerializer(direcciones, many=True)
        if direcciones:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    def post(self, request,*args,**kwargs):

        serializer = DireccionesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)        """