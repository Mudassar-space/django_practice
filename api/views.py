from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from api.serializers import StudentSerializer
from students.models import Student
# Create your views here.

@api_view(['GET', 'POST', ])
def studentsView(request):
    if request.method == 'GET':
        student = Student.objects.all()
        serializer = StudentSerializer(student, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    if request.method == "POST":
        serializer_data = StudentSerializer(data = request.data)
        serializer_data.is_valid(raise_exception=True)
        serializer_data.save()
        return Response(serializer_data.data, status=status.HTTP_201_CREATED)
    
@api_view(['GET','PUT', 'PATCH'])
def studentupdate(request, pk = None):
    student =  get_object_or_404(Student, pk = pk)
    print(student,"<<<<<<<<<<<<<<<<<<<<<")

    if request.method == 'GET':
        stu_serializer = StudentSerializer(student)  # Fix 2: Pass object, not data
        print(stu_serializer, "????????????????????")
        return Response(stu_serializer.data, status=status.HTTP_200_OK)
    
    if request.method == "PUT":
        stu_serializer = StudentSerializer(student, data = request.data)

    if request.method == "PATCH":
        stu_serializer = StudentSerializer(student, data = request.data, partial = True)
    
    if stu_serializer.is_valid():
        stu_serializer.save()
        return Response(stu_serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(stu_serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    

