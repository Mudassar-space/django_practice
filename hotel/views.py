from django.shortcuts import render
from rest_framework import viewsets, status
from hotel.serializers import HotelSerializers
from .models import HotelModel
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class HotelViewSet(viewsets.ModelViewSet):
    serializer_class = HotelSerializers
    queryset = HotelModel.objects.all()

    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


    # def list(self, request):
    #     hotel = HotelModel.objects.all()
    #     obj_hotel = HotelSerializers(hotel, many = True)
    #     return Response(obj_hotel.data)
    
    # def retrieve(self, request,pk = None):
    #     id = pk
    #     if id is not None:
    #         hotel = HotelModel.objects.get(id=id)
    #         hotel_ser = HotelSerializers(hotel)
    #         return Response(hotel_ser.data)
        
    # def create(self, request):
    #     serializer = HotelSerializers(data = request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     else:
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    # def update(self, request, pk = None):
    #     id = pk
    #     if id is not None:
    #         hotel = HotelModel.objects.get(id = id)
    #         serializer = HotelSerializers(hotel, data = request.data)
    #         if serializer.is_valid():
    #             serializer.save()
    #             return Response(serializer.data, status = status.HTTP_200_OK)
    #         else:
    #             return Response(serializer.errors)
    #     else:
    #         return Response("Not found.")
        

    # def partial_update(self, request, pk = None):
    #     id = pk
    #     if id is not None:
    #         hotel = HotelModel.objects.get(id = id)
    #         serializer = HotelSerializers(hotel, data = request.data, partial = True)
    #         if serializer.is_valid():
    #             serializer.save()
    #             return Response(serializer.data, status = status.HTTP_200_OK)
    #         else:
    #             return Response(serializer.errors)
    #     else:
    #         return Response("Not found.")
        
    
    # def destroy(self, request, pk = None):
    #     id  = pk
    #     hotel = HotelModel.objects.get(pk = id)
    #     hotel.delete()
    #     return Response("Successfully deleted", status=status.HTTP_204_NO_CONTENT)
        
    
             
        
    